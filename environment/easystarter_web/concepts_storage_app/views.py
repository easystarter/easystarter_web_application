from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.views import generic

from .models import Concept, Keywords
from .forms import ConceptForm


def index(request):
    concepts_storage = Concept.objects.all()
    keywords = Keywords.objects.all()
    return render_to_response('concepts_storage_app/index.html', {'concepts_storage': concepts_storage,
                                                                  'keywords': keywords})


def contacts(request):
    return render_to_response('concepts_storage_app/contacts.html')


class ConceptDetailView(generic.DetailView):
    model = Concept
    template_name = 'concepts_storage_app/details.html'

    def get_context_data(self, **kwargs):
        context = super(ConceptDetailView, self).get_context_data(**kwargs)
        context['slug'] = self.kwargs['slug']
        context['keywords'] = Keywords.objects.all()
        return context


def add_concept(request):
    if request.method == 'POST':
        form = ConceptForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            pub_date = datetime.strptime(form.cleaned_data['pub_date'], '%m/%d/%Y')
            goal = form.cleaned_data['goal']
            days_to_go = form.cleaned_data['days_to_go']
            Concept.objects.create(
                title=title,
                description=description,
                pub_date=pub_date,
                goal=goal,
                days_to_go=days_to_go
            ).save()
            return HttpResponseRedirect('/')
    else:
        form = ConceptForm()
    return render(request, 'concepts_storage_app/form.html', {'form': form})


def get_concepts_base_on_keywords(request, id):
    kwargs = {}

    kwargs['keywords'] = Keywords.objects.all()
    kwargs['keyw_s'] = Keywords.objects.get(id=id)
    kwargs['concepts'] = Concept.objects.filter(keywords__name__exact=kwargs['keyw_s'])
    return render(request, 'concepts_storage_app/keypage.html', kwargs)
