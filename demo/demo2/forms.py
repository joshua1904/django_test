from django.db.models import Model
from django.forms import ModelForm, DateInput, Form, CharField

from .models import Quote, Person


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = "__all__"
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"


class FilterForm(Form):
    name = CharField(max_length=200, required=False)