from datetime import datetime

from django.db import models


# Create your models here.


class SiteSetting(models.Model):
    code = models.CharField(verbose_name="Код", max_length=50, unique=True)
    name = models.CharField(verbose_name="Название", max_length=50)
    value = models.TextField(verbose_name="Значение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "настройка"
        verbose_name_plural = "настройки"
        ordering = ["-name"]


class News(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=250)
    text = models.TextField(verbose_name="Содержание")
    image = models.ImageField(verbose_name="Изображение")

    created_at = models.DateTimeField(verbose_name="Дата создания", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Активен", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"
        ordering = ["-created_at"]


class Program(models.Model):
    code = models.CharField(verbose_name="Код", max_length=50, unique=True)
    name = models.CharField(verbose_name="Наименование", max_length=250)
    description = models.CharField(verbose_name="Описание", max_length=500)
    image = models.ImageField(verbose_name="Изображение")

    created_at = models.DateTimeField(verbose_name="Дата создания", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Активен", default=True)

    def __str__(self):
        return self.code + " " + self.name

    class Meta:
        verbose_name = "программа"
        verbose_name_plural = "программы"
        ordering = ["-created_at"]


class Page(models.Model):
    code = models.CharField(verbose_name="Код страницы", max_length=50, unique=True)
    url = models.CharField(verbose_name="URL страницы", max_length=50)
    group = models.CharField(verbose_name="Код группы", max_length=20)
    group_name = models.CharField(verbose_name="Название группы", max_length=50, null=True, blank=True)
    title = models.CharField(verbose_name="Заголовок страницы", max_length=250)
    content = models.TextField(verbose_name="HTML содержание страницы")
    order = models.PositiveIntegerField(verbose_name="Порядок отображения в меню")
    
    created_at = models.DateTimeField(verbose_name="Дата создания", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Активен", default=True)
    fulltext_field = models.CharField(verbose_name="Поле для полнотекстового поиска", max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "страница"
        verbose_name_plural = "страницы"

    
# 


FILE_CATEGORY_CHOICES = [
    ('commoninfo', 'Основные сведения'),
    ('structure', 'Структура и органы управления'),
    ('documents', 'Основная документация'),
    ('education', 'Образование'),
    ('management', 'Руководство и педагогический состав'),
    ('equipment', 'Материально-техническое обеспечение. Доступная среда'),
    ('paidservices', 'Платные образовательные услуги'),
    ('finance', 'Финансово-хозяйственная деятельность'),
    ('studentinfo', 'Вакантные места. Стипендии'),

    ('applicants', 'Поступающим'),
    ('students', 'Студентам'),
    ('teachers', 'Учителям'),
    ('professionalitet', 'Профессионалитет'),
]


class File(models.Model):
    category = models.CharField(verbose_name="Категория", max_length=20, choices=FILE_CATEGORY_CHOICES, null=True, blank=True)
    code = models.CharField(verbose_name="Код", max_length=50, unique=True)
    name = models.CharField(verbose_name="Название", max_length=250)
    file = models.FileField(verbose_name="Файл", upload_to="files")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "файл"
        verbose_name_plural = "файлы"
        ordering = ["-name"]


class Feedback(models.Model):
    name = models.CharField(verbose_name="Имя отправителя", max_length=50)
    email = models.CharField(verbose_name="Email отправителя", max_length=50)
    message = models.TextField(verbose_name="Сообщение")
    
    created_at = models.DateTimeField(verbose_name="Дата создания", default=datetime.now)
    is_completed = models.BooleanField(verbose_name="Заявка обработана", default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "заявки"
