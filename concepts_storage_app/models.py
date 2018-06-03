import datetime
import pytz

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from .choices import *

utc = pytz.UTC


class Concept(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=20, blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Concept, self).save(*args, **kwargs)

    # description = models.TextField(max_length=2000)
    # description = RichTextField(max_length=2000)
    description = RichTextUploadingField(max_length=2000)
    status = models.CharField(max_length=20,
                              choices=STATUS, default='Draft')
    created = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField('Publication date')

    category = models.CharField(max_length=30,
                                choices=CATEGORY, default='')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'publication date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently ?'

    def __str__(self):
        return self.title

    goal = models.IntegerField(default=0, validators=[MaxValueValidator(100000000), MinValueValidator(0)])
    pledge = models.IntegerField(default=0, validators=[MaxValueValidator(100000000), MinValueValidator(0)])

    def funded(self):
        if self.pledge == 0 or self.goal == 0:
            return 0
        else:
            return round((self.pledge/self.goal)*100, 2)

    backers_counter = models.IntegerField(default=0)
    days_to_go = models.IntegerField(choices=DAYS_TO_GO, default=30)

    def get_days_left(self):
        days_left = str(
            (self.pub_date + datetime.timedelta(days=self.days_to_go)) - utc.localize(datetime.datetime.now())
        )[:7]
        return days_left
