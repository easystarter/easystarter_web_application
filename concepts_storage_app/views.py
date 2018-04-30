from datetime import datetime
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


class ConceptDetailView(generic.DetailView):
    model = Concept
    template_name = 'concepts_storage_app/details.html'

    def get_context_data(self, **kwargs):
        context = super(ConceptDetailView, self).get_context_data(**kwargs)
        context['slug'] = self.kwargs['slug']
        return context


def add_concept(request):
    if request.method == 'POST':
        form = ConceptForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            pub_date = datetime.strptime(form.cleaned_data['pub_date'], '%m/%d/%Y')
            category = form.cleaned_data['category']
            goal = form.cleaned_data['goal']
            days_to_go = form.cleaned_data['days_to_go']
            Concept.objects.create(
                title=title,
                description=description,
                pub_date=pub_date,
                category=category,
                goal=goal,
                days_to_go=days_to_go
            ).save()
            return HttpResponseRedirect('/')
    else:
        form = ConceptForm()
    return render(request, 'concepts_storage_app/form.html', {'form': form})
