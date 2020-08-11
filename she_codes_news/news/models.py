from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify 


class Category(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        ordering = ['category']
    
    def __str__(self):
        return self.category


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='stories'
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField()
    story_category = models.ManyToManyField(Category)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('news:story', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)