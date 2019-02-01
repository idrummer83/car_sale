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
        # create a form instance and populate it with data from the request:
        form = CarAddForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            Car.objects.create(
                name=form.cleaned_data.get('name'),
                price=int(form.cleaned_data.get('price')),
                year=int(form.cleaned_data.get('year')),
                car_mrk=form.cleaned_data.get('car_mrk'),
                car_mdl=form.cleaned_data.get('car_mdl')
            )
            return HttpResponseRedirect('/thanks/')

    else:
        form = CarAddForm()
    return render(request, 'car_form_add.html', {'form': form})
