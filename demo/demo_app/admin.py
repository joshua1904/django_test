from django.contrib import admin
from .models import TodoItem, Shopping, Item


admin.site.register(TodoItem)
admin.site.register(Shopping)
admin.site.register(Item)
# Register your models here.
