from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content']
        widgets = {
            'pub_date': forms.DateInput (
                format = ('%m/%d/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'title': forms.TextInput (
                attrs={
                    'class' : 'form-title'
                }
            ),
            'author': forms.TextInput (
                attrs={
                    'class' : 'form-author'
                }
            ),
            'pub_date': forms.TextInput (
                attrs={
                    'class' : 'form-pub_date'
                }
            ),
            'content': forms.Textarea (
                attrs={
                    'class' : 'form-content'
                }
            ),
        }

            # 'category': forms.ChoiceField (
            #     choices = [
            #         ('review', 'Review'),
            #         ('lifestyle', 'Lifestyle'),
            #         ('domestic', 'Domestic News'),
            #         ('international', 'International News')
            #     ],
            #     attrs = {
            #         'class': 'form-control',
            #         'placeholder': 'Select a category',
            #         'type': 'select',
            #     }
            # )