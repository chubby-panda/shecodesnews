from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField()

    def __str__(self):
        return str(self.title)