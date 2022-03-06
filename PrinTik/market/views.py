from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics

from .models import Category, Feedback, Product, ProductImage
from .serializers import(
    ProductCreateSerializer,
    ProductDetailSerializer,
    ProductImageSerializer,
    ProductsListSerializer,
    CategorySerializer,
    FeedbackSerializer,
    FeedbackCreateSerializer
)
    

class ProductDetailView(APIView):
    '''Отображение товара'''
        
    def get_object(self, pk):

        try:
            return Product.objects.get(pk=pk)
        
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk: int):
        '''Возвращение товаров'''

        product = self.get_object(pk)
        serializer = ProductDetailSerializer(product)
        
        return Response(serializer.data)

    def put(self, request, pk):
        '''Обновляение всех полей товаров'''

        product = self.get_object(pk)
        serialiser = ProductCreateSerializer(product, data=request.data)

        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        '''Частичное обновляение полей товаров'''

        product = self.get_object(pk)
        serialiser = ProductCreateSerializer(product, data=request.data, partial=True)

        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        '''Удаление товара'''

        product = self.get_object(pk)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductListView(APIView):
    '''Отображение списка товаров'''
    
    def post(self, request):
        '''Создание товар'''

        serializer = ProductCreateSerializer(data=request.data)

        if serializer.is_valid():
        
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        '''Возвращение список с товарами'''

        products = Product.objects.all()
        serializer = ProductsListSerializer(products, many=True)

        return Response(serializer.data)


class CategoryDetailView(APIView):
    '''Отображение категорий'''

    def get_object(self, pk):

        try:
            return Category.objects.get(pk=pk)
        
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk: int):
        '''Возвращение категории'''

        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        
        return Response(serializer.data)
        
    def put(self, request, pk):
        '''Обновляение всех полей категории'''

        category = self.get_object(pk)
        serialiser = CategorySerializer(category, data=request.data)

        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        '''Частичное обновляение полей категории'''

        category = self.get_object(pk)
        serialiser = CategorySerializer(category, data=request.data, partial=True)

        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        '''Удаление категории'''

        category = self.get_object(pk)
        category.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListView(APIView):
    '''Отображение списка катогорий'''
    
    def post(self, request):
        '''Создание катогории'''

        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
        
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        '''Возвращение список катогорий'''

        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)


class FeedbackDetailView(APIView):
    '''Отображение отзыва'''

    def get_object(self, pk):

        try:
            return Feedback.objects.get(pk=pk)
        
        except Feedback.DoesNotExist:
            raise Http404

    def get(self, request, pk: int):
        '''Возвращение отзыва'''

        feedback = self.get_object(pk)
        serializer = FeedbackSerializer(feedback)
        
        return Response(serializer.data)
        
    def put(self, request, pk):
        '''Обновляение всех полей отзыва'''

        feedback = self.get_object(pk)
        serialiser = FeedbackSerializer(feedback, data=request.data)

        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        '''Частичное обновляение полей отзыва'''

        feedback = self.get_object(pk)
        serialiser = FeedbackSerializer(feedback, data=request.data, partial=True)

        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        '''Удаление отзыва'''

        feedback = self.get_object(pk)
        feedback.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FeedbackListView(APIView):
    '''Отображение списка отзывов'''
    
    def post(self, request):
        '''Создание отзыв'''

        serializer = FeedbackCreateSerializer(data=request.data)

        if serializer.is_valid():
        
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        '''Возвращение список отзывов'''

        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)

        return Response(serializer.data)


class ProductImageViews(generics.ListAPIView):
    '''Детальное представление товаров'''

    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

