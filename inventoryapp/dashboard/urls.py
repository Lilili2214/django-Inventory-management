from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='home'),
    path("dashboard/", views.index, name='dashboard-index'),
    
    path("staff/", views.staff, name='dashboard-staff'),
    path("staff/<int:pk>/", views.staff_detail, name='staff-detail'),
    path("product/", views.product, name='dashboard-product'),
    path("order/", views.order, name='dashboard-order'),
    path('product/delete/<int:pk>/', views.delete, name='delete'),
    path('product/delete-product/<int:pk>/', views.deleteProduct, name='delete-product'),
    path('product/update/<int:pk>/', views.editProduct, name='edit-product'),
]
