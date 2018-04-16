from django.views import generic
from .models import Concept


class IndexView(generic.ListView):
    template_name = 'concepts_storage_app/index.html'
    context_object_name = 'concepts_storage'

    def get_queryset(self):
        return Concept.objects.all()
