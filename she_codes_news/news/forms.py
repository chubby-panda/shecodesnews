from django import forms
from django.forms import ModelForm, SplitDateTimeField, SplitDateTimeWidget

from .models import NewsStory

class StoryForm(ModelForm):
    pub_date = SplitDateTimeField(
        widget=SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        )
    )
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image', 'content']
        labels = {'image': "Image URL"}
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