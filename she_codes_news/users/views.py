from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from news.models import NewsStory


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'


class AuthorView(generic.DetailView):
    model = CustomUser


class UpdateAccountView(LoginRequiredMixin, generic.UpdateView):
    login_url = 'users/login/'
    model = CustomUser
    fields = ['password', 'email', 'bio', 'profile_img']
    template_name = 'users/customuser_update.html'

    def get_success_url(self):
        slug = self.kwargs['slug']
        success_url = reverse_lazy('users:author-detail', kwargs={'slug': slug})
        return success_url

def change_password(request, *args, **kwargs):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('users:author-detail', slug=request.user.slug)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })
