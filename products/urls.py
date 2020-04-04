from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('manufactorers/<int:pk>/', views.manufacturer_detail, name='manufactor-detail'),
    path('manufactorers/', views.manufacturer_list, name='manufactor-list'),

]
