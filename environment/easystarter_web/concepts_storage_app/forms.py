from django import forms

from .choices import *
from .models import Concept
from datetime import datetime
from ckeditor.widgets import CKEditorWidget


class ConceptForm(forms.Form):
    class Meta:

        model = Concept
        fields = ['title', 'description']

    title = forms.CharField(required=True, label='Title',
                            widget=forms.TextInput(attrs={'id': 'title'}))

    description = forms.CharField(widget=CKEditorWidget())

    date_now = datetime.now().date().strftime("%m/%d/%Y")
    pub_date = forms.CharField(required=True, label='Date of publication',
                               widget=forms.TextInput(attrs={'id': 'datepicker', 'width': '200',
                                                             'value': date_now}))

    category = forms.ChoiceField(required=True, label='Category', choices=CATEGORY,
                                 widget=forms.Select(attrs={'id': 'category'}), initial='')

    goal = forms.IntegerField(required=True, max_value=100000000, min_value=0, label='Goal',
                              widget=forms.TextInput(attrs={'aria-label': 'Amount (to the nearest dollar)',
                                                            'type': 'text',
                                                            'id': 'goal'}))

    days_to_go = forms.ChoiceField(required=True, choices=DAYS_TO_GO, label='Days to go',
                                   widget=forms.RadioSelect(attrs={'id': 'choice',
                                                                   'class': 'list-unstyled'}))


class MessageForm(forms.Form):
    name = forms.CharField(required=True, max_length=50,
                           widget=forms.TextInput(attrs={
                                                    'class': 'form-control col-md-8 col-sm-12 col-xs-12',
                                                    'id': 'Name',
                                                    'aria-describedby': 'nameHelp',
                                                    'placeholder': '',
                                                    'type': 'text'
                                                    }))

    email = forms.EmailField(required=True, max_length=50, label='Email',
                             widget=forms.EmailInput(attrs={
                               'class': 'form-control col-md-8 col-sm-12 col-xs-12',
                               'id': 'Email1',
                               'aria-describedby': 'emailHelp',
                               'placeholder': 'Enter',
                               'type': 'email'
                           }))

    phone = forms.CharField(required=True, label='Phone number',
                            widget=forms.TextInput(attrs={
                                                    'class': 'form-control col-md-8 col-sm-12',
                                                    'id': 'Phone',
                                                    'aria-invalid': 'false',
                                                    'placeholder': '+00000000000',
                                                    'type': 'tel',
                                                    'size':  '10',
                                                    'name': 'tel'
                               }))

    message = forms.CharField(required=True, max_length=1000,  label='Message',
                              widget=forms.Textarea(attrs={
                                   'class': 'form-control col-md-8 col-sm-12',
                                   'id': 'exampleFormControlTextarea1',
                                   'rows': '3'
                              }))
