from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('author/<int:pk>/', views.AuthorView.as_view(), name='author-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)