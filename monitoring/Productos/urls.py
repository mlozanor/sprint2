from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.producto_view, name='producto_view'),
    path('<int:pk>/', views.producto_view, name='producto_view'),
]

