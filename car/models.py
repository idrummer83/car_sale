from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=255, verbose_name='Категория')
    min_date = models.SmallIntegerField(verbose_name='min_date')
    max_date = models.SmallIntegerField(verbose_name='max_date')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class CarMark(models.Model):
    car_mark = models.CharField(max_length=255, verbose_name='Марка авто')

    def __str__(self):
        return self.car_mark

    class Meta:
        verbose_name = 'Марка авто'
        verbose_name_plural = 'Марка авто'



class CarModel(models.Model):
    car_model = models.CharField(max_length=255, verbose_name='Модель авто')

    def __str__(self):
        return self.car_model

    class Meta:
        verbose_name = 'Модель авто'
        verbose_name_plural = 'Модель авто'


class Car(models.Model):

    price = models.SmallIntegerField(verbose_name='Цена')
    year = models.SmallIntegerField(verbose_name='Год выпуска')
    name = models.CharField(max_length=255, verbose_name='Имя владельца')

    car_cat = models.CharField(verbose_name='Категория', max_length=255, default='do 1990')
    car_mrk = models.ForeignKey(CarMark, verbose_name='Марка', related_name='car_marks', on_delete=models.CASCADE)
    car_mdl = models.ForeignKey(CarModel, verbose_name='Модель', related_name='car_models', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'