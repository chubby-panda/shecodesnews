from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.template.defaultfilters import slugify


class CustomUser(AbstractUser):

    profile_img = models.ImageField(upload_to='images', default="default.jpg")
    bio = models.TextField(max_length=1000, blank=True, default='')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:author-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)