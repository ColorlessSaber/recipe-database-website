"""
URL configuration for recipes app
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('new-recipe/', views.new_recipe, name='new-recipe'),
    path('cookbook/', views.cookbook, name='cookbook'),
    path('recipe/<int:recipe_id>/', views.recipe_details, name='recipe-details'),
    path('recipe/<int:recipe_id>/edit/', views.edit_recipe, name='edit-recipe'),
]
