from django import forms

from .choices import *
from .models import Concept, Category

from datetime import datetime
from ckeditor.widgets import CKEditorWidget


class ConceptForm(forms.Form):
    class Meta:

        model = Concept
        fields = ['title', 'description']

    title = forms.CharField(required=True, max_length=50, label='Title',
                            widget=forms.TextInput(attrs={'id': 'title'}))

    description = forms.CharField(widget=CKEditorWidget())

    date_now = datetime.now().date().strftime("%m/%d/%Y")
    pub_date = forms.CharField(required=True, label='Date of publication',
                               widget=forms.TextInput(attrs={'id': 'datepicker', 'width': '200',
                                                             'value': date_now}))

    list_of_categories = [(category.name, category.name) for category in Category.objects.all()]
    print(list_of_categories)
    category = forms.ChoiceField(required=True, label='Category', choices=list_of_categories,
                                 widget=forms.Select(attrs={'id': 'category'}), initial='')

    goal = forms.IntegerField(required=True, max_value=100000000, min_value=0, label='Goal',
                              widget=forms.TextInput(attrs={'aria-label': 'Amount (to the nearest dollar)',
                                                            'type': 'text',
                                                            'id': 'goal'}))

    days_to_go = forms.ChoiceField(required=True, choices=DAYS_TO_GO, label='Days to go',
                                   widget=forms.RadioSelect(attrs={'id': 'choice',
                                                                   'class': 'list-unstyled'}))
