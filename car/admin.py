"""Регистрация моделей в админ панели. Для создания и изменения через админку"""

from django.contrib import admin

from car.models import *


# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    """
    list_display - Какие поля будут отображаться в админ панели
    list_filter - по каким полям будет разрешено фильтровать
    """
    list_display = ('id', 'category')
    list_filter = ('category',)


@admin.register(CarMark)
class AdminCarMark(admin.ModelAdmin):
    list_display = ('id', 'car_mark')
    list_filter = ('car_mark',)


@admin.register(CarModel)
class AdminCarModel(admin.ModelAdmin):
    list_display = ('id', 'car_model')
    list_filter = ('car_model',)


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ('id', 'price', 'year', 'name', 'car_mrk', 'car_mdl')
    list_filter = ('price', 'year', 'name')


@admin.register(Photo)
class AdminPhoto(admin.ModelAdmin):
    list_display = ('title', 'photo', 'car', 'created_at')
    list_filter = ('title', 'car', 'created_at')
