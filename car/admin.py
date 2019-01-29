from django.contrib import admin
from car.models import *

# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_filter = ('category',)



@admin.register(Car)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'marka', 'model', 'price', 'year', 'name')
    list_filter = ('marka', 'model', 'price', 'year', 'name')