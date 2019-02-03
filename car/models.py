from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=255, verbose_name='категория')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class CarMark(models.Model):
    car_mark = models.CharField(max_length=255, verbose_name='marka avto')

    def __str__(self):
        return self.car_mark

    class Meta:
        verbose_name = 'CarMark'
        verbose_name_plural = 'CarMark'



class CarModel(models.Model):
    car_model = models.CharField(max_length=255, verbose_name='model avto')

    def __str__(self):
        return self.car_model

    class Meta:
        verbose_name = 'CarModel'
        verbose_name_plural = 'CarModel'


class Car(models.Model):

    price = models.SmallIntegerField()
    year = models.SmallIntegerField()
    name = models.CharField(max_length=255)

    car_cat = models.CharField(verbose_name='Категория', max_length=255, default='do 1990')
    car_mrk = models.ForeignKey(CarMark, verbose_name='Marka', related_name='car_marks', on_delete=models.CASCADE)
    car_mdl = models.ForeignKey(CarModel, verbose_name='Models', related_name='car_models', on_delete=models.CASCADE)

    # def year_categry(self):
    #     if int(self.year) < 1990:
    #         self.car_cat = 'do 90'
    #     else:
    #         self.car_cat = 'posle 90'


    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'