import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from markdown import markdown


class Concept(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently ?'

    def __str__(self):
        return self.title



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
