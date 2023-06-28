from django.db import models

from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username
