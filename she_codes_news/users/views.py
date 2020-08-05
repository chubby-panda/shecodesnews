from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from django.views.generic import DetailView
from .models import CustomUser
from .forms import CustomUserCreationForm


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserProfileView(DetailView):
    template_name = 