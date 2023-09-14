from django.contrib import admin
from django.urls import path
from . import views
from .views import calculate

urlpatterns = [
    path('rekenmachine/', views.home, name='rekenmachine'),
    path('calculate/', calculate, name='calculate'),
]



