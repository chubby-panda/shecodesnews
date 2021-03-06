from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify 


class Category(models.Model):
    category = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        ordering = ['category']
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('news:category-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='stories'
    )
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    story_category = models.ManyToManyField(Category, related_name='stories')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_plural = "news stories"

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('news:story', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    @property
    def approved_comments(self):
        return self.comments.filter(approved=True)
        


class Comment(models.Model):
    story = models.ForeignKey(NewsStory, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f"Comment [{self.content}] by {self.name}."

    def approve(self):
        self.approved = True
        self.save()