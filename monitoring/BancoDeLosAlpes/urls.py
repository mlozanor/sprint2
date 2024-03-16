from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.banco_view, name='banco_view'),
    path('<int:pk>/', views.banco_view, name='banco_view'),
]