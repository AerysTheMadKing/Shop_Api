from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField
from category.models import Category


User = get_user_model()


class Product(models.Model):
    STATUS_CHOICES = (
        ('in_stock', 'В Наличии'),
        ('out_of_stuck', 'Нет в наличии'),
    )


    owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='products')
    title = models.CharField(max_length=150)
    description = RichTextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.RESTRICT)
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.CharField(choices=STATUS_CHOICES, max_length=20)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title