from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from markdown import markdown


class Concept(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    # pub_date = models.DateTimeField('date published')



#     markdown_description_field = models.TextField()
#     html_description_field = models.TextField(editable=False)
#
#     def __unicode__(self):
#         return self.title
#
#
# def save(self):
#     self.html_description_field = markdown(self.markdown_description_field)
#     super(Concept, self).save()
