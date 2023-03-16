from django.contrib import admin
from .models import User, Contact, Feedback

# Register your models here.

admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Feedback)
