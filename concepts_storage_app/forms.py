from django import forms
from .choices import *


class ConceptForm(forms.Form):
    title = forms.CharField(required=True, max_length=50, label='Name of the project', widget=forms.TextInput)
    description = forms.CharField(required=True, max_length=500,
                                  label='Description of the project',
                                  widget=forms.Textarea)
    pub_date = forms.DateField(label='Published Date', required=True,
                               widget=forms.SelectDateWidget,
                               input_formats=['%d %B, %Y'])
    category = forms.ChoiceField(choices=CATEGORY, label='Category', required=True,  widget=forms.Select, initial='')

    # goal = models.IntegerField(default=0)
    # pledge = models.IntegerField(default=0)
    #
    # def funded(self):
    #     return (self.pledge / self.goal) * 100
    #
    # backers_counter = models.IntegerField(default=0)
    # day_to_go = models.CharField(max_length=100, choices=(
    #     (SHORT_TERM, '30 days to go, platform fee is 5% of the project cost'),
    #     (MIDDLE_TERM, '45 days to go, platform fee is 10% of the project cost'),
    #     (LONG_TERM, '60 days to go, platform fee is 15% of the project cost')),
    #                              default=SHORT_TERM)
