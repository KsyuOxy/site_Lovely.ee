from django.urls import path
from .views import product_details, products_list, update_product, delete_product, create_product

urlpatterns = [
    path('<int:product_id>/product_details', product_details, name='product_details'),
    path('products_list', products_list, name='products_list'),
    path('<int:product_id>/update_product', update_product, name='update_product'),
    path('<int:product_id>/delete_product', delete_product, name='delete_product'),
    path('create_product', create_product, name='create_product'),
]
