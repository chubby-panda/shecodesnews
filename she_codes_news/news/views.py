from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import NewsStory, Category, Comment
from .forms import StoryForm, UpdateStoryForm, CommentForm


def handler404(request, exception):
    return render(request, '404.html', status=404)


class AddStoryView(LoginRequiredMixin, generic.CreateView):
    login_url = '/users/login/'
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        """Return all news stories."""
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        """Filter the stories in the queryset to get only the latest five."""
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:3]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context


def story_detail(request, slug):
    template_name = 'news/story.html'
    story = get_object_or_404(NewsStory, slug=slug)
    comments = story.comments.all()
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current story to the comment
            new_comment.story = story
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
        else:
            messages.error(request, 'Please login or register to leave a comment.')
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'story': story,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

@login_required
def approve_comment(request, pk, slug):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('news:story', slug=slug)


@login_required
def remove_comment(request, pk, slug):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.name or request.user == comment.story.author:
        comment.delete()
    return redirect('news:story', slug=slug)


class CategoryView(generic.DetailView):
    model = Category


class UpdateStoryView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    login_url = 'users/login/'
    model = NewsStory
    form_class = UpdateStoryForm
    context_object_name = 'storyForm'
    template_name = 'news/updateStory.html'

    def get_success_url(self):
        """Get the story_id from the request object to pass to the success url"""
        slug = self.kwargs['slug']
        success_url = reverse_lazy('news:story', kwargs={'slug': slug})
        return success_url

    def test_func(self):
        """Only let the user access this page if they are the author of the object being updated"""
        return self.get_object().author == self.request.user

class DeleteStoryView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    login_url = 'users/login/'
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')
    
    def test_func(self):
        """Only let the user access this page if they are the author of the object being deleted"""
        return self.get_object().author == self.request.user


class SearchView(generic.TemplateView):
    template_name = 'news/search.html'


class SearchResultsView(generic.ListView):
    model = NewsStory
    template_name = 'news/searchResults.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        qs =  NewsStory.objects.filter(
            Q(content__icontains=query) | Q(title__icontains=query) | Q(author__username__icontains=query) | Q(story_category__category__icontains=query) | Q(author__first_name__icontains=query) | Q(author__last_name__icontains=query)
            )
        return qs.distinct