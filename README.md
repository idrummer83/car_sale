# car_sale
car sale app based on python 3, django 2


Тестовое задание
Вы участвуете в проекте разработки площадки для продажи автомобилей. На первом этапе администратор будет вручную добавлять все предложения о продаже автомобилей через админ-панель, но в будущем это смогут делать и посетители сайта. Также планируется разработка API для подключения мобильных приложений.
Ваши задачи:
1) Разработать страницу со списком (таблицей) автомобилей. Колонки:
 Id
 Марка
 Модель
 Категория (см. ниже пункт 3)
 Цена
Должна быть возможность сортировать список по каждой из колонок. Сортировка по марке и модели
должна сортировать в алфавитном порядке по имени марки/модели.
Должна быть возможность фильтровать список по году выпуска (от и до).
2) Возможность добавить автомобиль. Поля формы:
 Марка (выбор из списка)
 Модель (выбор из списка)
 Год выпуска
 Цена
 Имя владельца (текстовое поле)
Все поля обязательные для заполнения.
3) После успешного добавления автомобиля, ему должна автоматически назначаться одна из
следующих категорий:
 До 1990 года выпуска
 От 1990 до 2000 года выпуска
 От 2000 до 2010 года выпуска
 После 2010 года выпуска
Категория должна выбираться на основании введенного года выпуска.
Управление категориями и справочниками реализовывать не нужно. Реализация сидеров для
наполнения базы приветствуется.
