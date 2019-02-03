from django.shortcuts import render
from django.http import HttpResponseRedirect
from car.models import *
from car.forms import CarAddForm

# Create your views here.

def cars_list(request):

    car_list = Car.objects.all()

    context = {
        'car_list': car_list,
    }

    return render(request, 'base.html', context)


def car_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request.POST['year'])
        # create a form instance and populate it with data from the request:
        form = CarAddForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if int(request.POST['year']) < 1990:
                Car.car_cat = 'do 90'
            else:
                Car.car_cat = 'posle 90'
            car = form.save(commit=False)
            car.save()
            return render(request, 'car_list.html')

    else:
        form = CarAddForm()
    return render(request, 'car_form_add.html', {'form': form})
