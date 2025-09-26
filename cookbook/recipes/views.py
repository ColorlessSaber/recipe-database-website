from django.shortcuts import render
from .forms import RecipesForm, IngredientGroupFormSet, IngredientsFormSet
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
        print("save form!")
        return render(request, 'recipes/recipes-home.html') #TODO update later
    else:
        recipe_form = RecipesForm()
        ingredient_group_formset = IngredientGroupFormSet()
        context = {
            'recipe_form': recipe_form,
            'ingredient_group_formset': ingredient_group_formset,
        }
        return render(request, 'recipes/new-recipe.html', context)

def cookbook(request):
    """
    Opens the webpage showing everything in the cookbook.

    :param request:
    :return:
    """
    return render(request, 'recipes/cookbook.html')