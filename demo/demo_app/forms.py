from django.forms import ModelForm, DateInput
from . models import Shopping, Item

class ShoppingForm(ModelForm):
    class Meta:
        model = Shopping
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }

class ItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ["shopping"]

