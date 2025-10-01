from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RecipesForm, IngredientsFormSet
from .models import Recipes, IngredientGroup, Ingredients

# Create your views here.
def home(request):
    """
    Generates the home page.

    :param request:
    :return:
    """
    return render(request, 'recipes/recipes-home.html')

def new_item(request):
    """
    Creates a new recipe.

    :param request:
    :return:
    """
    if request.method == "POST":
        recipe_form = RecipesForm(request.POST)
        if recipe_form.is_valid():
            new_recipe = recipe_form.save()
            return redirect('new-ingredient-group', recipe_pk=new_recipe.pk)
        else:
            messages.error(request, 'Invalid form was submitted. Please try again.')
    else:
        recipe_form = RecipesForm()

    context = {
        'recipe_form': recipe_form,
    }
    return render(request, 'recipes/new-recipe.html', context)

def new_ingredient_group(request, recipe_pk):
    """
    Creates a new ingredient group and associated ingredients, and links the group to the recipe.

    This function is used adding new ingredient groups to existing and new recipes.

    :param request:
    :param recipe_pk: The primary key of the recipe that the new ingredient group will be associated with.
    :return:
    """
    recipe = get_object_or_404(Recipes, pk=recipe_pk)
    print(recipe_pk)
    return render(request, 'recipes/cookbook.html')

def cookbook(request):
    """
    Opens the webpage showing everything in the cookbook.

    :param request:
    :return:
    """
    return render(request, 'recipes/cookbook.html')