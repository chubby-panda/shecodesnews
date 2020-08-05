from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    # This is where you could define extra attributes, e.g. bio, profile pic...

    def __str__(self):
        return self.username

class UserProfile(models.Model):

    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE)
