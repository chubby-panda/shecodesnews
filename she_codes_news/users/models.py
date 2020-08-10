from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):

    profile_img = models.ImageField(upload_to='images', default="default.jpg")
    bio = models.TextField(max_length=1000, default="This user hasn't written a bio yet!")

    def __str__(self):
        return self.username
    
    