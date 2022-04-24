from django import forms

from car.models import *


class CarAddForm(forms.ModelForm):
    photo_field = forms.ImageField(label='Фото', widget=forms.ClearableFileInput(attrs={'multiple': True,
                                                                                        'class': 'form-control'}))

    class Meta:
        model = Car
        fields = ('price', 'year', 'name', 'car_mrk', 'car_mdl')
        # fields = '__all__'
