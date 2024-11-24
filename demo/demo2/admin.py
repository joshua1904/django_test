from django.contrib import admin

# Register your models here.
from .models import Person, Quote
# Register your models here.


admin.site.register(Person)
admin.site.register(Quote)
