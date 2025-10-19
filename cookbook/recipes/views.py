from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from .forms import RecipesForm, IngredientsFormSet,  IngredientGroupForm
from .models import Ingredients

# Create your views here.
def home(request):
    """
    Generates the home page.

    :param request:
    :return:
    """
    return render(request, 'recipes/recipes-home.html')

def new_recipe(request):
    """
    Creates a new recipe.

    :param request:
    :return:
    """
    if request.method == "POST":
        recipe_form = RecipesForm(request.POST, prefix="recipe_form")
        ingredient_group_form = IngredientGroupForm(request.POST, prefix="ingredient_group_form")
        ingredient_formset = IngredientsFormSet(request.POST, prefix="ingredient_formset")

        if recipe_form.is_valid() and ingredient_formset.is_valid() and ingredient_group_form.is_valid():
            try:
                with transaction.atomic():
                    recipe = recipe_form.save()

                    ingredient_group_form.instance.recipe_ref = recipe
                    ingredient_group = ingredient_group_form.save()

                    ingredient_formset.instance = ingredient_group
                    ingredient_formset.save()

                messages.success(request, f'Recipe {recipe.name} has been saved successfully!')
                return redirect("recipes-home")
            except Exception as e:
                messages.error(request, f'There was an error when saving recipe: {e}')
        else:
            messages.error(request, 'Invalid form was submitted. Please try again.')
    else:
        recipe_form = RecipesForm(prefix="recipe_form")
        ingredient_group_form = IngredientGroupForm(prefix="ingredient_group_form")
        ingredient_formset = IngredientsFormSet(prefix="ingredient_formset")

    return render(request, 'recipes/new-recipe.html', {
        'recipe_form': recipe_form,
        'ingredient_group_form': ingredient_group_form,
        'ingredient_formset': ingredient_formset,
        'measurements': Ingredients.MEASUREMENT_CHOICES,
    })

def cookbook(request):
    """
    Opens the webpage showing everything in the cookbook.

    :param request:
    :return:
    """
    return render(request, 'recipes/cookbook.html')