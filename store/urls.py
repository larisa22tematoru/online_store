from django import views
from . import views
from django.urls import path

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='home'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    # path('shop/<slug:subcategory_slug>/', views.subcategory_list, name='subcategory_list'),

]