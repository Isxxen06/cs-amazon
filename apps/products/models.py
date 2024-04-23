from django.db import models
from apps.categories.models import Category
from apps.images.models import Image


class Product(models.Model):
    class CurrencyChoice(models.TextChoices):
        dollar = 'dollar'
        som = 'som'
        euro = 'euro'
    name = models.CharField(max_length=250, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ManyToManyField(Image, related_name="product_images", verbose_name="Картинки")
    price = models.IntegerField(default=0, verbose_name="Цена")
    currency = models.CharField(max_length=150, choices=CurrencyChoice.choices, verbose_name="Валюта")
    category = models.ManyToManyField(Category, related_name="product_categories", verbose_name="Категория")
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

