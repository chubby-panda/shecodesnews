from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'image', 'content']
        widgets = {
            'pub_date': forms.DateInput (
                format = ('%m/%d/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
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