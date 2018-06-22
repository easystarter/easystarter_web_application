import datetime
import pytz

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField

from .choices import *

utc = pytz.UTC


class Keywords(models.Model):
    class Meta:
        db_table = 'keywords'
    name = models.CharField(max_length=50, unique=True, verbose_name='Tags')

    def __str__(self):
        return self.name


class Concept(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Concept, self).save(*args, **kwargs)

    description = RichTextUploadingField(max_length=15000)
    status = models.CharField(max_length=50,
                              choices=STATUS, default='Draft')
    created = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField('Publication date')

    category = models.CharField(max_length=50, blank=True, choices=CATEGORY)
    keywords = models.ManyToManyField(Keywords, related_name='keywords',
                                      related_query_name='keyword',
                                      verbose_name='Tags')

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
        days = datetime.timedelta(days=self.days_to_go).days-(datetime.date.today() - self.pub_date.date()).days
        return days if days > 0 else 0
