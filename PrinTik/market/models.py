from itertools import product
import re
from tabnanny import verbose
from django.db import models


class Category(models.Model):
    '''Категории товаров'''

    name = models.CharField(max_length=255, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'
    
    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    '''Класс товар'''

    name = models.CharField(max_length=255, verbose_name='Товар')
    description = models.TextField(verbose_name='Описание')
    create_datetime = models.DateTimeField(verbose_name='Время публикации товара', auto_now_add=True)
    update_datetime = models.DateTimeField(verbose_name='Время обновление информации о товаре', auto_now=True)

    category = models.ForeignKey(Category, verbose_name='Катогория', on_delete=models.SET_NULL, null=True, related_name='products')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self) -> str:
        return self.name


class ProductImage(models.Model):
    '''Картинки товаров'''

    image = models.ImageField(verbose_name='Ссылка')

    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Картинка товара'
        verbose_name_plural = 'Картинки товаров'
    
    def url(self):
        return self.image.url


class Feedback(models.Model):
    '''Отзовы товара'''

    author = models.CharField(max_length=255, verbose_name='Автор')
    text = models.TextField(verbose_name='Отзыв')
    create_datetime = models.DateTimeField(verbose_name='Время публикации отзыва', auto_now_add=True)
    
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.SET_NULL, null=True, related_name='feedbacks')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    
    def short_text(self):
        '''Короткий текст отзыва'''

        return self.text[:100]