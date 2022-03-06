from django.urls import path

from .views import (
    CategoryDetailView,
    FeedbackListView,
    ProductDetailView,
    ProductListView, 
    CategoryListView, 
    FeedbackDetailView,
    ProductImageViews
)


urlpatterns = [
    path('product/', ProductListView.as_view(), name='product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-edit'),
    
    path('category/', CategoryListView.as_view(), name='category'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category-edit'),

    path('feedback/', FeedbackListView.as_view(), name='feedback'),
    path('feedback/<int:pk>', FeedbackDetailView.as_view(), name='feedback-edit'),

    path('image/', ProductImageViews.as_view(), name='image'),
]