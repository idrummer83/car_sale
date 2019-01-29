from django.shortcuts import render
from car.models import *

# Create your views here.

def cars_list(request):

    car_list = Car.objects.all()

    context = {
        'car_list': car_list,
    }

    return render(request, 'car_list.html', context)
