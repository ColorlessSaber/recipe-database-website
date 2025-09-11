"""
URL configuration for recipes app
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='recipes-home'),
]
