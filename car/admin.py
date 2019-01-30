from django.contrib import admin
from car.models import *

# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_filter = ('category',)


@admin.register(CarMark)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'car_mark')
    list_filter = ('car_mark',)


@admin.register(CarModel)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'car_model')
    list_filter = ('car_model',)


@admin.register(Car)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'price', 'year', 'name')
    list_filter = ('price', 'year', 'name')