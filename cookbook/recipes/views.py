from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RecipesForm, IngredientsFormSet, IngredientsForm, IngredientGroupForm
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
            #new_recipe = recipe_form.save()
            foo = 1
            return redirect('new-ingredient-group', recipe_pk=foo)
        else:
            messages.error(request, 'Invalid form was submitted. Please try again.')
    else:
        recipe_form = RecipesForm()

    return render(request, 'recipes/new-recipe.html', {
        'recipe_form': recipe_form,
    })

def new_ingredient_group(request, recipe_pk):
    """
    Creates a new ingredient group with associated ingredients and links the group to the recipe.

    This function adds a new ingredient groups to existing and new recipes.

    :param request:
    :param recipe_pk: The primary key of the recipe that the new ingredient group will be associated with.
    :return:
    """
    #recipe = get_object_or_404(Recipes, pk=recipe_pk) # TODO look into get the name of the recipe and adding it to the HTML view
    if request.method == "POST":
        ingredient_group_form = IngredientGroupForm(request.POST)
        ingredient_formset = IngredientsFormSet(request.POST)
        if ingredient_formset.is_valid() and ingredient_group_form.is_valid():
            #new_ingredient_group = ingredient_formset.save(commit=False)
            # TODO finish this section once screen is working
            print("new ingredient group saved")
            return redirect("recipes-home")
        else:
            messages.error(request, 'Invalid form was submitted. Please validate all entry(s) have been filled/selected, and then try again.')
    else:
        ingredient_group_form = IngredientGroupForm()
        ingredient_formset = IngredientsFormSet()

    return render(request, 'recipes/ingredient-group.html', {
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