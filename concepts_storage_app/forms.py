from django import forms
from .choices import *


class ConceptForm(forms.Form):
    title = forms.CharField(required=True, max_length=50, label='Title',
                            widget=forms.TextInput(attrs={'id': 'title'}))
    description = forms.CharField(required=True, max_length=500, label='Description',
                                  widget=forms.Textarea(attrs={'id': 'description'}))
    pub_date = forms.DateField(required=True, label='Publication date',
                               widget=forms.SelectDateWidget(attrs={'id': 'pub_date'}),
                               input_formats=['%d %B, %Y'])
    category = forms.ChoiceField(choices=CATEGORY, label='Category', required=True,
                                 widget=forms.Select(attrs={'class': 'form-control',
                                                            'id': 'category'}),
                                 initial='')

    goal = forms.IntegerField(required=True, max_value=100000000, min_value=0, label='Goal',
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'aria-label': 'Amount (to the nearest dollar)',
                                                            'type': 'text',
                                                            'id': 'goal'}))
    days_to_go = forms.ChoiceField(required=True, choices=DAYS_TO_GO, label='Days to go',
                                   widget=forms.Select(attrs={'id': 'choice',
                                                              'class': 'form-check-input',
                                                              'name': 'optionsRadios',
                                                              'checked': "",
                                                              'type': 'radio'}))
