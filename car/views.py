from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from car.forms import CarAddForm
from car.models import *


# Create your views here.

def cars_list(request):
    car_list = Car.objects.all().prefetch_related("photo_set")

    context = {
        'car_list': car_list,
    }

    return render(request, 'car_list.html', context)


def car_form(request):
    if request.method == 'POST':
        form = CarAddForm(request.POST, request.FILES)
        # print(form._errors)
        if form.is_valid():
            year = form.cleaned_data['year']
            price = form.cleaned_data['price']
            name = form.cleaned_data['name']
            car_mrk = form.cleaned_data['car_mrk']
            car_mdl = form.cleaned_data['car_mdl']

            cat = Category.objects.all()
            car_category = ''
            for i in cat:
                if int(year) <= i.max_date and int(year) >= i.min_date:
                    car_category = i.category

            qwe = Car(
                year=year, price=price, name=name, car_cat=car_category, car_mrk=car_mrk, car_mdl=car_mdl
            )
            photos = request.FILES.getlist('photo_field')
            qwe.save()
            for ph in photos:
                photo = Photo(photo=ph, car=qwe)
                photo.save()
            return render(request, 'thank_you.html')

    else:
        form = CarAddForm()
    return render(request, 'car_form_add.html', {'form': form})


def rest(request):
    my_model = Car.objects.all()
    response = serializers.serialize("json", my_model)
    return HttpResponse(response, content_type='application/json')
