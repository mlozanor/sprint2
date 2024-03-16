from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.proveedor_view, name='proveedor_view'),
    path('<int:pk>/', views.proveedor_view, name='proveedor_view'),
]