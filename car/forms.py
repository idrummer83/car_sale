
from django import forms
from car.models import *

class CarAddForm(forms.Form):
    price = forms.CharField()

    # class Meta:
    #     model = Car
    #     fields = ('price', 'year', 'name', 'car_cat', 'car_mrk', 'car_mdl')