from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add-story/', views.AddStoryView.as_view(), name='newsStory'),
    path('<slug:slug>/', views.StoryView.as_view(), name='story'),
    path('<slug:slug>/edit-story/', views.UpdateStoryView.as_view(), name='edit-story'),
    path('<slug:slug>/delete-story/', views.DeleteStoryView.as_view(), name='delete-story'),
]
