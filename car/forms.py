"""Создание и настройка форм, для создания моделей"""

from django import forms

from car.models import *

class CarAddForm(forms.ModelForm):
    """
    label - название поля в форме
    widget - тип формы(в этом случае множественный выбор фото
    """
    photo_field = forms.ImageField(label='Фото', widget=forms.ClearableFileInput(attrs={'multiple': True,
                                                                                        'class': 'form-control'}))
    class Meta:
        """
        model  - связанная модель на основе которой будет создаваться форма
        fields  - какие поля будут включени в форму
        """
        model = Car
        fields = ('price', 'year', 'name', 'car_mrk', 'car_mdl')
        # fields = '__all__'
