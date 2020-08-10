from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import NewsStory
from .forms import StoryForm



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
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'


class UpdateStoryView(LoginRequiredMixin, generic.UpdateView):
    login_url = 'users/login/'
    model = NewsStory
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/updateStory.html'

    def get_success_url(self):
        story_id = self.kwargs['pk']
        success_url = reverse_lazy('news:story', kwargs={'pk': story_id})
        return success_url