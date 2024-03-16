from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.codeudor_view, name='codeudor_view'),
    path('<int:pk>/', views.codeudor_view, name='codeudor_view'),
]