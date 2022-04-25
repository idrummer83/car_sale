from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from car.forms import CarAddForm
from car.models import *


# Create your views here.

def cars_list(request):
    """
    Car.objects.all() - выбор всех объектов модели
    .prefetch_related - загрузка связанный обхектов модели

    render -  принимает текущий request, html страницу и словарь с данным которые можно использовать в шаблоне
    """
    car_list = Car.objects.all().prefetch_related("photo_set")

    context = {
        'car_list': car_list,
    }

    return render(request, 'car_list.html', context)


def car_form(request):
    """
    request.method - тип запроса (GET, POST)
    form = CarAddForm(request.POST, request.FILES) - Загружаем данные из request в форму для валидации
     form.is_valid() - проверка валидности

    """
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

            # Поиск категории по дате
            for i in cat:
                if int(year) <= i.max_date and int(year) >= i.min_date:
                    car_category = i.category

            # Создание и сохранение объекта машины
            qwe = Car(
                year=year, price=price, name=name, car_cat=car_category, car_mrk=car_mrk, car_mdl=car_mdl
            )
            qwe.save()

            # Создание и сохранение полученных фото и прикрепленние к только что созданной машины
            photos = request.FILES.getlist('photo_field')
            for ph in photos:
                photo = Photo(photo=ph, car=qwe)
                photo.save()
            return render(request, 'thank_you.html')

    else:
        form = CarAddForm()
    return render(request, 'car_form_add.html', {'form': form})


def rest(request):
    """Возвращение объектов модели в виде json"""
    my_model = Car.objects.all()
    response = serializers.serialize("json", my_model)
    return HttpResponse(response, content_type='application/json')
