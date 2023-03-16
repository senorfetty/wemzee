from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name ='login_user'),
    path('signup/', views.signup, name ='signup'),
    path('logout_user/', views.logout_user, name = 'logout_user'),    
    path('home/', views.home, name ='home'),
    path('about/', views.about, name ='about'),
    path('contact/', views.contact, name ='contact'),
    path('feedback/', views.feedback, name ='feedback'),
    path('sendsms/', views.sendsms, name ='sendsms'), 
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name= 'activate'),
    path('passreset/', views.passreset, name ='passreset'),
    path('blog/', views.blog, name ='blog'),
    path('detail/', views.detail, name ='detail'),
    path('gadgets/', views.gadgets, name ='gadgets'),    
    # path('sendsms/', views.sendsms, name ='sendsms'), 
    # path('sendsms/', views.sendsms, name ='sendsms'), 
]