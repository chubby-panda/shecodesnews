from django.contrib import admin
from .models import NewsStory, Category


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'image', 'content',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(NewsStory, StoryAdmin)
admin.site.register(Category)