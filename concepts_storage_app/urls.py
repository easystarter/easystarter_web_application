from django.urls import path
from . import views

app_name = 'concepts_storage_app'
urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
]