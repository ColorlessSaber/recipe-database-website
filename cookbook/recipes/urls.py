"""
URL configuration for recipes app
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('new-recipe/', views.new_item, name='new-recipe'),
    path('cookbook/', views.cookbook, name='cookbook'),
]
