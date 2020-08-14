from django.contrib import admin
from .models import NewsStory, Category, Comment


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'image', 'content',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'story', 'pub_date', 'approved')
    list_filter = ('approved', 'pub_date')
    search_fields = ('name', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

admin.site.register(NewsStory, StoryAdmin)
admin.site.register(Category)