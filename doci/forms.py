from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Feedback, Contact
from django.forms import ModelForm

class RegForm(UserCreationForm):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    email= forms.EmailField(max_length=100)

    class Meta:
        model = User 
        fields= ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

# class ContactForm(ModelForm):
#     email=forms.EmailField()
#     sub=[
#         ('INQUIRY','INQUIRY'),
#         ('REVIEW','REVIEW'),
#     ]
#     subject= forms.ChoiceField(choices=sub)
#     message= forms.Textarea()

#     class Meta:
#         model= Contact
#         fields= '__all__'


# # class FeedbackForm(ModelForm):
# #     message= forms.CharField(max_length=100)
# #     email= forms.EmailField()

    
# #     class Meta:
# #         model= Feedback
# #         fields= '__all__'
