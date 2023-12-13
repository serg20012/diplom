from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.index, name='index'),
    path('add_product/', views.add_product, name='add_product'),
    path('products/', views.product_list, name='product_list'),
    path('add_purchase/', views.add_purchase, name='add_purchase'),
    path('add_hol/', views.add_holiday, name='add_hol'),
    # path('form/', views.many_fields_form, name='form'),
]