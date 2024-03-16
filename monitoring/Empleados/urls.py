from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.empleado_view, name='empleado_view'),
    path('<int:pk>/', views.empleado_view, name='empleado_view'),
]