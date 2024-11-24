from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.db.models import F
from .forms import QuoteForm, PersonForm, FilterForm
from .models import Quote, Person

# Create your views here.

class QuoteList(ListView):
    model = Quote
    context_object_name = "quotes"
    template_name = "quote_list.html"
    form_class = FilterForm
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = self.form_class(self.request.GET)
        if self.form.is_valid():
            name = self.form.cleaned_data.get("name")
            if name:
                # FIlter with foregin key annotate to join tables and F to get the attribute of the foregin key
                return queryset.annotate(name=F("person__name")).filter(name=name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context


class AddQuote(CreateView):
    form_class = QuoteForm
    template_name = "add_quote.html"
    success_url = "/demo_2"

def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    form = PersonForm()
    return render(request, "add_quote_person.html", {"form": form})

class DeleteQuote(DeleteView):
    model = Quote
    success_url = "/demo_2"
    template_name = "delete_quote.html"