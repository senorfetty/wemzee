from django.db import models

# Create your models here.

class User(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    username= models.CharField(max_length=50)
    email= models.EmailField(max_length=100)

    def __str__(self):
        return self.username

class Contact(models.Model):
    # first_name= models.CharField(max_length=100)
    email=models.EmailField()
    sub=[
        ('INQUIRY','INQUIRY'),
        ('REVIEW','REVIEW'),
    ]
    subject= models.CharField(max_length=7, choices=sub,default=None)
    message= models.TextField(max_length=200)

    def __str__(self):
        return self.email

class Feedback(models.Model):
    email= models.EmailField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.email
    

class items(models.Model):
    name= models.CharField(max_length=200)
    price= models.DecimalField(max_digits=6, decimal_places=2)
    image= models.ImageField()
    onoffer= models.BooleanField(default=False)


