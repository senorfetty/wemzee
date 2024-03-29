"""trial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from doci import views
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doci.urls')),
    path('', views.login_user),
    path('passreset/done/', PasswordResetDoneView.as_view(template_name='doci/templates/passresetdone.html'), name= 'passresetdone'),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='doci/templates/passresetconfirm.html'), name= 'passresetconfirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='doci/templates/passresetcomplete.html'), name= 'passresetcomplete'),
]