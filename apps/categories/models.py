from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    image = models.FileField(upload_to="category_image", verbose_name="Картина")
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name