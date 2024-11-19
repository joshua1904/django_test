from django.db import models
from django.urls import reverse


class TodoItem(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField()
    
class Shopping(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.date} {self.name}"
    
    def get_absolute_url(self) -> str:
        return reverse('Hallo', kwargs={'pk': self.pk})

    def get_absolute_add_item_url(self):
        return reverse("add Item", kwargs={"pk": self.pk})

    def get_absolute_delete_shopping_url(self):
        return reverse("delete-shopping", kwargs={"pk": self.pk})
    

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE)
