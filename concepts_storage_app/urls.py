from django.urls import path
from . import views

app_name = 'concepts_storage_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('concept/add', views.add_concept, name='add_concept')
]
