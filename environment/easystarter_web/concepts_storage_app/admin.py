from django.contrib import admin
from .models import Concept, Keywords


@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main', {
            'fields': ('title', 'description', 'slug')
        }),
        ('Date', {
            'fields': ('pub_date',)
        }),
        ('Funds', {
            'fields': ('goal', 'days_to_go', 'pledge', 'backers_counter')
        }),
        ('Additional information', {
            'fields': ('category', 'status')
        }),
        ('Special', {
            'fields': ('slug', 'keywords')
        })
    )
    list_display = ('title', 'created', 'pub_date', 'goal',
                    'pledge', 'backers_counter', 'days_to_go', 'status')
    list_filter = ('status', 'pub_date', 'category')


@admin.register(Keywords)
class KeywordsAdmin(admin.ModelAdmin):
    fields = ['name']

