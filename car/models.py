from django.db import models


# Create your models here.

class Category(models.Model):
    """
    Создание полей модели
    models.CharField - тип поля
    max_length - длинна поля
    verbose_name - человеческое название поля
    """
    category = models.CharField(max_length=255, verbose_name='Категория')
    min_date = models.SmallIntegerField(verbose_name='min_date')
    max_date = models.SmallIntegerField(verbose_name='max_date')

    def __str__(self):
        # Выводит название модели при выводе объекта модели как строки
        return self.category

    class Meta:
        # Названия для единственного и множественного числа модели (отображается в админ панели)
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
    """
        Создание полей модели
        default - дефолтное значение которое автоматически вставляется если не указано друго
        related_name - имя модели для обращения к нему через связанную модель
        on_delete - тип удаления связанной модели при удалении
        models.CASCADE - удаляет связанную молель
        models.SETNULL - вставляет вместо связанной модели None
        models.SETDEFAULT - вставляет вместо связанной дефолтное значение

    """
    price = models.SmallIntegerField(verbose_name='Цена')
    year = models.SmallIntegerField(verbose_name='Год выпуска')
    name = models.CharField(max_length=255, verbose_name='Имя владельца')

    car_cat = models.CharField(verbose_name='Категория', max_length=255, default='do 1990')
    car_mrk = models.ForeignKey(CarMark, verbose_name='Марка', related_name='car_marks', on_delete=models.CASCADE)
    car_mdl = models.ForeignKey(CarModel, verbose_name='Модель', related_name='car_models', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Photo(models.Model):
    """
        Создание полей модели
        upload_to - путь где будут храниться фото
        blank - может ли поле быть пустым
        auto_now_add - автоматическое добавление времени при создании обхекта модели
    """
    title = models.CharField(max_length=100, blank=True)
    photo = models.ImageField('фото', upload_to='photo/%Y/%m/%d/', blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фото'
