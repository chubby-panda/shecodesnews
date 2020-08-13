from django.urls import path
from . import views

app_name = 'news'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('search/results/', views.SearchResultsView.as_view(), name='search-results'),
    path('add-story/', views.AddStoryView.as_view(), name='newsStory'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='category-detail'),
    path('<slug:slug>/', views.StoryView.as_view(), name='story'),
    path('<slug:slug>/edit-story/', views.UpdateStoryView.as_view(), name='edit-story'),
    path('<slug:slug>/delete-story/', views.DeleteStoryView.as_view(), name='delete-story'),
]

handler404 = views.handler404