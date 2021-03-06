from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta: 
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_img']
        labels = {'bio': 'About', 'profile_img': 'Profile Image'}

class CustomUserChangeForm(UserChangeForm):

    class Meta: 
        model = CustomUser
        fields = ['username', 'email']

