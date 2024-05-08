from django.db import models
from apps.users.models import User
from apps.products.models import Product

class Review(models.Model):
    class RatingChoice(models.IntegerChoices):
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name="Продукт")
    comment = models.TextField(max_length=500, verbose_name="Комментарий")   
    rating = models.IntegerField(choices=RatingChoice.choices, verbose_name="Оценка")
    created_at = models.DateField(auto_created=True,   verbose_name="Дата создания")
    
      
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.comment