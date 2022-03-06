from dataclasses import field
from itertools import product
from pickletools import read_floatnl
from unicodedata import category
from pyparsing import empty
from rest_framework import serializers

from .models import Category, Feedback, Product, ProductImage


class FeedbackListSerializer(serializers.ModelSerializer):
    '''Сериализатор отзывов'''

    class Meta:
        model = Feedback
        exclude = ('product', )


class ProductImageSerializer(serializers.ModelSerializer):
    '''Сериализатор изображений'''

    class Meta:
        model = ProductImage
        fields = ('id', 'url')


class ProductDetailSerializer(serializers.ModelSerializer):
    '''Сериализатор товара'''

    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    images = ProductImageSerializer(many=True)
    feedbacks = FeedbackListSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'create_datetime', 'update_datetime', 'category', 'images', 'feedbacks')


class ProductCreateSerializer(serializers.ModelSerializer):
    '''Сериализатор создания товара'''

    class Meta:
        model = Product
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    '''Сериализатор категорий'''
    
    class Meta:
        model = Category
        fields = ('id', 'name') 


class CategoryCreateSerializer(serializers.ModelSerializer):
    '''Сериализатор создания категории'''

    class Meta:
        model = Category
        fields = ('name',)


class ProductsListSerializer(serializers.ModelSerializer):
    '''Сериализатор списка товаров'''

    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'create_datetime', 'update_datetime', 'category', 'images')


class FeedbackSerializer(serializers.ModelSerializer):
    '''Сериализатор отзывов'''

    product = serializers.SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        model = Feedback
        fields = '__all__'

class FeedbackCreateSerializer(serializers.ModelSerializer):
    '''Сериализатор создания отзыва'''

    class Meta:
        model = Feedback
        fields = '__all__'



# class FeedbackCreateSerializer(serializers.ModelSerializer):
#     '''Создает отзыв на товар'''

#     class Meta:
#         model = Feedback
#         fields = '__all__'


# class FeedbackDetailSerializer(serializers.ModelSerializer):
#     '''Сериализатор отзыва'''

#     class Meta:
#         model = Feedback
#         fields = ('author', 'text', 'create_datetime', 'product')


# class ProductImageListSerialiser(serializers.ModelSerializer):
#     '''Сериализатор картинок'''

#     class Meta:
#         model = ProductImage
#         fields = ('id', 'image')


# class ProductDetailSerializer(serializers.ModelSerializer):
#     '''Сериализатор товара'''

#     category = serializers.SlugRelatedField(slug_field='name', read_only=True)
#     feedbacks = FeedbackListSerializer(many=True)
#     #images = ProductImageListSerialiser(many=True)

#     class Meta:
#         model = Product
#         fields = ('name', 'description', 'create_datetime', 'update_datetime', 'category', 'feedbacks')
