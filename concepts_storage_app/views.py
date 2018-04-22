from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import Concept
from .forms import ConceptForm


class IndexView(generic.ListView):
    template_name = 'concepts_storage_app/index.html'
    context_object_name = 'concepts_storage'

    def get_queryset(self):
        return Concept.objects.all()


def add_concept(request):
    if request.method == 'POST':
        form = ConceptForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            pub_date = form.cleaned_data['pub_date']
            category = form.cleaned_data['category']
            Concept.objects.create(
                title=title,
                description=description,
                pub_date=pub_date,
                category=category
            ).save()
            return HttpResponseRedirect('/')
    else:
        form = ConceptForm()
    return render(request, 'concepts_storage_app/form.html', {'form': form})
