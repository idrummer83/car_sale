
from django import forms
from car.models import *

class CarAddForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('price', 'year', 'name', 'car_mrk', 'car_mdl')