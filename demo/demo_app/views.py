from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import TodoItem, Item, Shopping
from django.views.generic import ListView, DetailView, DeleteView
from .forms import ShoppingForm, ItemForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "base2.html")

def show_shoppings(request):
    shoppings = Shopping.objects.all()
    return render(request, "shoppings.html", {"shoppings": shoppings})


class ShoppingList(ListView):
    model = Shopping
    context_object_name = 'shoppings'
    template_name = 'shopping_list.html'


class ShoppingDetailView(DetailView):
    model = Shopping
    context_object_name = "shopping_details"
    template_name = "shopping_detail.html"



def add_shopping_form(request):
    if request.method == "POST":
        form = ShoppingForm(request.POST)
        if form.is_valid():
            form.save()

    form = ShoppingForm()
    return render(request, "add_shopping_form.html", {"form": form})


def add_item_form(request, pk: int):
    current_shopping = get_object_or_404(Shopping, id=pk)
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.shopping = current_shopping
            new_item.save()
            messages.success(request, "Item wurde erfolgreich hinzugefügt.")
            return redirect("add Item", pk=pk)
        else:
            messages.error(request, "Falsche Eingabe")
            return HttpResponse(request, "yeet")
    form = ItemForm()
    return render(request, "add_item_form.html", {"form": form, "shopping": current_shopping})

class DeleteShopping(DeleteView):
    model = Shopping
    success_url = "/list"
    template_name = "delete_shopping.html"

def delete_item(request, item_pk: int, shopping_pk: int):
    if request.method == "POST":
        item = get_object_or_404(Item, pk=item_pk)
        item.delete()
        return redirect("Hallo", pk=shopping_pk)
    return redirect("Hallo", pk=shopping_pk)
