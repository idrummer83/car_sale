from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Car(Category):
    marka = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.SmallIntegerField()

    category = models.ForeignKey(Category, verbose_name='Категория', related_name='categories', on_delete=models.CASCADE)

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'