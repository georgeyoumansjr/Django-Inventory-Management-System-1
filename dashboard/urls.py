
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('',views.dashboard_index, name='dashboard_index'),
    path('add-products/', views.add_products, name='add_products'),
    path('search-products/', views.search_available_products, name='search_available_products'),
    path('view-available-products/', views.view_available_products, name='view_available_products'),
    path('sell-available-products/', views.sell_available_products, name='sell_available_products'),
    path('view-sold-products/', views.view_sold_products, name='view_sold_products'),
    path('users/', views.users, name='users'),
]
