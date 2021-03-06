from django.urls import path
from .views import index, html_main_page, multipage, sign_in, register, catalog, \
    delivery, contacts, reviews, promotion, logout_user, result, ajax_reg, ajax_log_passwd

urlpatterns = [
    path('', index),
    path('main_page', html_main_page, name='home'),
    path('multi_page/<int:page_id>', multipage),
    path('login', sign_in, name='login'),
    path('register', register, name='register'),
    path('catalog', catalog, name='catalog'),
    path('delivery', delivery, name='delivery'),
    path('contacts', contacts, name='contacts'),
    path('reviews', reviews, name='reviews'),
    path('promotion', promotion, name='promotion'),
    path('logout', logout_user, name='logout'),
    path('result', result, name='result'),
    path('ajax_reg', ajax_reg, name='ajax_reg'),
    path('ajax_log_passwd', ajax_log_passwd, name='ajax_log_passwd'),
]
