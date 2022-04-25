"""car_sale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from car import views


# Каждый url в urlpatterns принимает три аргумента
# 1. ссылку на страницу
# 2. функция, которая будет вызываться при переходе на эту ссылку
# 3. имя ссылки для быстрого обращения

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^$', views.cars_list, name='main_page'),
                  url(r'^add-form/$', views.car_form, name='car_form'),
                  url(r'^get_rest/$', views.rest)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
