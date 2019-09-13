from django import forms
from django.forms import widgets
from webapp.models import status_choices


class ArticleForm(forms.Form):
    description = forms.CharField(max_length=3000, required=True, label='Description')
    status = forms.ChoiceField(choices=status_choices, required=False, label='Status')
    text = forms.CharField(max_length=3000, required=False, label='Text',
                           widget=widgets.Textarea)
    created_at = forms.DateField(label='Date', initial=None, required=False,
                                 widget=widgets.DateInput(attrs={'type': 'date'}))
