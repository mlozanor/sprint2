from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.prospecto_view, name='prospecto_view'),
    path('<int:pk>/', views.prospecto_view, name='prospecto_view'),
]