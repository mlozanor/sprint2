from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.solicitudes_view, name='solicitud_view'),
    path('<int:pk>/', views.solicitudes_view, name='solicitud_view'),
]