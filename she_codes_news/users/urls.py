from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import CreateAccountView, AccountDetailView


app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('account/', AccountDetailView.as_view(), name='account-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)