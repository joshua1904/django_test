from django.db import models
from django.db.models import DateField, ForeignKey, CharField


class Person(models.Model):
    name = CharField(max_length=30)

    def __str__(self):
        return self.name

class Quote(models.Model):
    quote = CharField(max_length=500)
    date = DateField()
    person = ForeignKey(Person, on_delete=models.CASCADE)


    def __str__(self):
        return self.quote



