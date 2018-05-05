from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list2, name='product_list'),
    #path('shop/category/<slug>/', views.product_list_by_category, name='product_list_by_category'),
    path('shop/category/<slug>/', views.product_list2, name='product_list_by_category'),

    path('shop/product/<slug>/', views.product_detail, name='product_detail'),
]