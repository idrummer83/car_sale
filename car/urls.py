
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cars_list, name='car_list'),
]