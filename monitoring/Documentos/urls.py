from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.documento_view, name='documento_view'),
    path('<int:pk>/', views.documento_view, name='documento_view'),
]