from django.db import models


# Create your models here.


class SiteSetting(models.Model):
    code = models.CharField(verbose_name="Код", max_length=50, unique=True)
    name = models.CharField(verbose_name="Название", max_length=50)
    value = models.TextField(verbose_name="Значение")

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

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Program(models.Model):
    code = models.CharField(verbose_name="Код", max_length=50, unique=True)
    name = models.CharField(verbose_name="Наименование", max_length=250)
    description = models.CharField(verbose_name="Описание", max_length=500)
    image = models.ImageField(verbose_name="Изображение")

    created_at = models.DateTimeField(verbose_name="Дата создания", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Активен", default=True)

    class Meta:
        verbose_name = "программа"
        verbose_name_plural = "программы"
        ordering = ["-created_at"]
