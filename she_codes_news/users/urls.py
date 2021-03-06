from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('author/<slug:slug>/', views.AuthorView.as_view(), name='author-detail'),
    path('author/<slug:slug>/edit/', views.UpdateAccountView.as_view(), name='author-update'),
    path('author/<slug:slug>/change-password/', views.change_password, name='change-password')
]