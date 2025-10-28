"""
URL configuration for recipes app
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('new-recipe/', views.new_recipe, name='new-recipe'),
    path('cookbook/', views.cookbook, name='cookbook'),
    path('recipe/<int:recipe_id>/details', views.recipe_details, name='recipe-details'),
    path('recipe/<int:recipe_id>/edit/', views.edit_recipe, name='edit-recipe'),
    path('recipe/<int:recipe_id>/new-ingredient-group/', views.new_ingredient_group, name='new-ingredient-group'),
    path('recipe/<int:recipe_id>/<int:ingredient_group_id>/edit/', views.edit_ingredient_group, name='edit-ingredient-group'),
    path('recipe/<int:recipe_id>/delete/', views.delete_recipe, name='delete-recipe'),
    path('recipe/<int:recipe_id>/<int:ingredient_group_id>/delete/', views.delete_ingredient_group, name='delete-ingredient-group'),
]
