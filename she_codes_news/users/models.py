from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):

    # This is where you could define extra attributes, e.g. bio, profile pic...

    def __str__(self):
        return self.username
    