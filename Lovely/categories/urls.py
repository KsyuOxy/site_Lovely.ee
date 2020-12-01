from django.urls import path
from .views import index, category_list, create_category, category_details, delete_category, update_category

urlpatterns = [
    path('', index, name='categories_homepage'),
    path('list', category_list, name='category_list'),
    path('create', create_category, name='create_category'),
    path('<int:category_id>/details', category_details, name='category_details'),
    path('<int:category_id>/delete', delete_category, name='delete_category'),
    path('<int:category_id>/update', update_category, name='update_category'),
]
