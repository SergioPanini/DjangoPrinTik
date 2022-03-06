from django.contrib import admin

from .models import Product, Category, Feedback, ProductImage


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    '''Админка товаров'''

    list_display = ('name', 'category', 'description', 'create_datetime', 'update_datetime')
    edit_fields = ('name', 'category', 'description')

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    '''Админка категорий'''
    
    list_display = ('name',)
    edit_fields = ('name',)


@admin.register(Feedback)
class AdminFeedBack(admin.ModelAdmin):
    '''Админка отзывов'''

    list_display = ('author', 'short_text')

@admin.register(ProductImage)
class AdminProductImage(admin.ModelAdmin):

    list_display = ('image','product')


