from django.urls import path
from . import views

app_name = 'concepts_storage_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('concept/<slug:slug>', views.ConceptDetailView.as_view(), name='details'),
    path('keywords/<int:id>', views.get_concepts_base_on_keywords, name='keywords'),
    path('add', views.add_concept, name='add_concept')
]
