from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from .forms import RecipesForm, IngredientsFormSet,  IngredientGroupForm
from .models import Ingredients, Recipes, IngredientGroup


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

                messages.success(request, f'Recipe {recipe.name} has been successfully saved!')
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
    Opens the webpage showing everything in the cookbook--IE, all the recipes that
    are saved in the database.

    :param request:
    :return:
    """
    list_of_categories = Recipes.CATEGORY_CHOICES

    if request.method == "POST":
        if request.POST.get("filter") != "all":
            recipes = Recipes.objects.filter(category=request.POST.get("filter")).order_by("name")
        else:
            recipes = Recipes.objects.all().order_by("name")
    else:
        recipes = Recipes.objects.all().order_by("name")

    return render(request, 'recipes/cookbook.html', {
        'list_of_categories': list_of_categories,
        'recipes': recipes,
    })

def recipe_details(request, recipe_id):
    """
    Loads the details of an individual recipe along with the ingredient group(s) and the ingredients per group.

    :param request:
    :param recipe_id: The id of the recipe user wishes to see
    :return:
    """
    recipe = get_object_or_404(Recipes, id=recipe_id)

    return render(request, 'recipes/recipe-details.html', {
        'recipe': recipe,
    })

def edit_recipe(request, recipe_id):
    """
    Opens webpage to allow user to edit the selected recipe.

    :param request:
    :param recipe_id: The id of the recipe user wishes to edit
    :return:
    """
    recipe = get_object_or_404(Recipes, id=recipe_id)
    if request.method == "POST":
        recipe_form = RecipesForm(request.POST, prefix="recipe_form", instance=recipe)
        recipe = recipe_form.save()
        messages.success(request, f'Recipe {recipe.name} has been successfully saved!')
        return redirect('recipe-details', recipe_id=recipe_id)
    else:
        recipe_form = RecipesForm(instance=recipe, prefix="recipe_form")
        return render(request, 'recipes/edit-recipe.html', {
            'recipe': recipe,
            'recipe_form': recipe_form,
        })

def delete_recipe(request, recipe_id):
    """
    Deletes an individual recipe from the database.

    :param request:
    :param recipe_id: The id of the recipe user wishes to delete
    :return:
    """
    recipe = get_object_or_404(Recipes, id=recipe_id)
    recipe.delete()
    messages.success(request, f'Recipe {recipe.name} has been successfully deleted!')
    return redirect('recipes-home')