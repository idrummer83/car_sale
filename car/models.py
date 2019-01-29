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

    date_category = {
        'before_1990': 1990,
        '1990-2000': 2000,
        '2000-2010': 2010,
        'after_2010': 2010,
    }

    marka = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.SmallIntegerField()
    year = models.SmallIntegerField()
    name = models.CharField(max_length=255)

    car_category = models.ForeignKey(Category, verbose_name='Категория', related_name='categories', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'