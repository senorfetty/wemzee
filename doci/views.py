from django.shortcuts import render, redirect
from .forms import RegForm
from .models import Feedback,Contact
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from twilio.rest import Client #Fettywap@1738679
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form= RegForm(request.POST)
        
        if form.is_valid():
            user= form.save(commit=False)
            user.is_active= False
            user.save()

            #domain of current site
            current_site= get_current_site(request)
            mail_subject= 'Activation Link has been sent to you'

            message= render_to_string('email.html',{
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)            
            })
            
            to_email= form.cleaned_data.get('email')
            email= EmailMessage(mail_subject,message,to=[to_email])
            email.send()
            return HttpResponse('Please confirm Email and complete registration')

    else:
        form = RegForm()
    return render(request, 'signup.html', {'form': form})
   
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        print (username, password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request,'INVALID CREDENTIALS')
            return redirect('login_user')   

    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def feedback(request):    
    if request.method == 'POST':
        feed=Feedback()
        email= request.POST.get('email')
        message= request.POST.get('message')

        feed.email= email
        feed.message= message

        feed.save()
        messages.success(request, 'Feedback has been Received.')
        return redirect('feedback')     
    else:
        return render(request, 'feedback.html')

def contact(request):
    if request.method == 'POST':
        cont=Contact()
        email= request.POST.get('email')
        subject= request.POST.get('subject')
        message= request.POST.get('message')

        cont.email= email
        cont.subject= subject
        cont.message= message

        cont.save()
        try:
            send_mail(
                subject,
                message,
                cont.email,
                ['senorfetty@gmail.com'],
                fail_silently=False,
            )
            print(subject,email, message)
        except BadHeaderError:
            return HttpResponse('invalid')
        messages.success(request, 'Thank You for Contacting Us.')  
        return redirect('contact')
    
    else:
        return render(request, 'contact.html')

def sendsms(request):
    account_sid= 'AC62262c9a488c2d5719bb588a8ed5090c'
    auth_token= '176307708ac777802c901aedb7c98fdb'
    client= Client(account_sid,auth_token)

    message= client.messages.create(
        to='+254792593059',
        from_= '+17574149542',
        body= 'We Mzee wasemaje'
    )
    print(message.sid)
    return HttpResponse('Message of we mzee sent to {message.to}')

def activate(request, uidb64, token):
    User= get_user_model()
    try:
        uid= force_str(urlsafe_base64_decode(uidb64))
        user= User.objects.get(pk=uid)
    except{TypeError, ValueError, OverflowError, User.DoesNotExist}:
        user=None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active= True
        user.save()
        return redirect('login_user')
    else:
        return HttpResponse('Activation Link Invalid')

def passreset(request):
    if request.method == 'POST':
        form= PasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            users= User.objects.filter(Q(email=data))

            if users.exists():
                for user in users:
                    subject= 'Password Reset Request'
                    
                    msg= render_to_string('passresetemail.html', {
                        'email': user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'WE MZEE',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),                        
                    })
                    
                    try:
                        send_mail(subject,msg,'senorfetty@gmail.com', [user.email],fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse ('Invalid Header Found')
                    return redirect('passreset/done')
    
    form= PasswordResetForm()
    return render(request, 'passreset.html', {'form': form})

def blog(request):
    return render(request, 'blog.html')

def detail(request):
    return render(request, 'detail.html')

def gadgets(request):
    return render(request, 'class.html')