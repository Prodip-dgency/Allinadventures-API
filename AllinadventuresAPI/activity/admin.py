from django.contrib import admin

from .models import Activity, Location, Category, Gallery, Content

# Register your models here.

admin.site.register([Activity, Location, Category, Gallery, Content])