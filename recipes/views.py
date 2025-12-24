from django.shortcuts import render, redirect, get_object_or_404
from django.template.response import TemplateResponse
from django.views import View
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

class NewRecipeView(View):
    """
    Opens the webpage to allow user to create a new recipe.
    """

    def get(self, request):
        recipe_form = RecipesForm(prefix="recipe_form")
        ingredient_group_form = IngredientGroupForm(prefix="ingredient_group_form")
        ingredient_formset = IngredientsFormSet(prefix="ingredient_formset")
        return TemplateResponse(request, 'recipes/new-recipe.html', {
            'recipe_form': recipe_form,
            'ingredient_group_form': ingredient_group_form,
            'ingredient_formset': ingredient_formset,
            'measurements': Ingredients.MEASUREMENT_CHOICES,
        })

    def post(self, request):
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

                messages.success(request, f'Recipe "{recipe.name}" has been successfully saved!')
                return redirect("recipes-home")
            except Exception as e:
                messages.error(request, f'There was an error when saving recipe: {e}')
        else:
            messages.error(request, 'Invalid form was submitted. Please try again.')

        return TemplateResponse(request, 'recipes/new-recipe.html', {
            'recipe_form': recipe_form,
            'ingredient_group_form': ingredient_group_form,
            'ingredient_formset': ingredient_formset,
            'measurements': Ingredients.MEASUREMENT_CHOICES,
        })

class CookbookView(View):
    """
    Opens the webpage showing everything in the cookbook--IE, all the recipes that
    are saved in the database.
    """

    def _list_of_categories(self):
        return {'list_of_categories': Recipes.CATEGORY_CHOICES}

    def get(self, request):
        recipes = Recipes.objects.all().order_by("name")
        context = self._list_of_categories() | {'recipes': recipes}
        return TemplateResponse(request, 'recipes/cookbook.html', context)

    def post(self, request):
        list_of_categories = Recipes.CATEGORY_CHOICES
        if request.POST.get("filter") != "all":
            recipes = Recipes.objects.filter(category=request.POST.get("filter")).order_by("name")
        else:
            recipes = Recipes.objects.all().order_by("name")

        context = self._list_of_categories() | {'recipes': recipes}
        return TemplateResponse(request, 'recipes/cookbook.html', context)

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

class EditRecipeView(View):
    """
    Opens webpage to allow user to edit the selected recipe.
    """

    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipes, id=recipe_id)
        recipe_form = RecipesForm(instance=recipe, prefix="recipe_form")
        return TemplateResponse(request, 'recipes/edit-recipe.html', {
            'recipe': recipe,
            'recipe_form': recipe_form,
        })

    def post(self, request, recipe_id):
        recipe = get_object_or_404(Recipes, id=recipe_id)
        recipe_form = RecipesForm(request.POST, prefix="recipe_form", instance=recipe)

        if recipe_form.is_valid():
            recipe = recipe_form.save()
            messages.success(request, f'Recipe "{recipe.name}" has been successfully saved!')
            return redirect('recipe-details', recipe_id=recipe_id)
        else:
            messages.error(request, 'Invalid form was submitted. Please try again.')

        return TemplateResponse(request, 'recipes/edit-recipe.html', {
            'recipe': recipe,
            'recipe_form': recipe_form,
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

        if recipe_form.is_valid():
            recipe = recipe_form.save()
            messages.success(request, f'Recipe "{recipe.name}" has been successfully saved!')
            return redirect('recipe-details', recipe_id=recipe_id)
        else:
            messages.error(request, 'Invalid form was submitted. Please try again.')
    else:
        recipe_form = RecipesForm(instance=recipe, prefix="recipe_form")
    return render(request, 'recipes/edit-recipe.html', {
        'recipe': recipe,
        'recipe_form': recipe_form,
    })

def edit_ingredient_group(request, ingredient_group_id, recipe_id):
    """
    Opens webpage to allow user to edit the selected ingredient group.

    :param request:
    :param ingredient_group_id: The id of the ingredient group user wishes to edit
    :param recipe_id: The id of the recipe the ingredient group is associated with
    :return:
    """
    ingredient_group = get_object_or_404(IngredientGroup, id=ingredient_group_id)
    recipe = get_object_or_404(Recipes, id=recipe_id)
    if request.method == "POST":
        ingredient_group_form = IngredientGroupForm(request.POST, instance=ingredient_group, prefix="ingredient_group_form")
        ingredient_formset = IngredientsFormSet(request.POST, instance=ingredient_group, prefix="ingredient_formset")

        if ingredient_group_form.is_valid() and ingredient_formset.is_valid():
            ingredient_group = ingredient_group_form.save()
            ingredient_formset.instance = ingredient_group
            ingredient_formset.save()

            messages.success(request, f'Ingredient Group "{ingredient_group.name}" has been successfully saved!')
            return redirect('recipe-details', recipe_id=recipe_id)
        else:
            messages.error(request, 'Invalid form was submitted. Please try again.')

    else:
        ingredient_group_form = IngredientGroupForm(instance=ingredient_group, prefix="ingredient_group_form")
        ingredient_formset = IngredientsFormSet(instance=ingredient_group, prefix="ingredient_formset")

    return render(request, 'recipes/ingredient-group.html', {
        'ingredient_group_form': ingredient_group_form,
        'ingredient_formset': ingredient_formset,
        'measurements': Ingredients.MEASUREMENT_CHOICES,
        'recipe': recipe,
        'edit_html': True,
    })

def new_ingredient_group(request, recipe_id):
    """
    Creates a new ingredient group for selected recipe.

    :param request:
    :param recipe_id: the id of the recipe the new ingredient group will be created for.
    :return:
    """
    recipe = get_object_or_404(Recipes, id=recipe_id)
    if request.method == "POST":
        ingredient_group_form = IngredientGroupForm(request.POST, prefix="ingredient_group_form")
        ingredient_formset = IngredientsFormSet(request.POST, prefix="ingredient_formset")

        if ingredient_formset.is_valid() and ingredient_group_form.is_valid():
            try:
                with transaction.atomic():
                    ingredient_group_form.instance.recipe_ref = recipe
                    ingredient_group = ingredient_group_form.save()

                    ingredient_formset.instance = ingredient_group
                    ingredient_formset.save()

                messages.success(request, f'Ingredient Group "{ingredient_group.name}" has been successfully saved!')
                return redirect('recipe-details', recipe_id=recipe_id)
            except Exception as e:
                messages.error(request, f'There was an error when saving ingredient group: {e}')
        else:
            messages.error(request, 'Invalid form was submitted. Please try again.')

    else:
        ingredient_group_form = IngredientGroupForm(prefix="ingredient_group_form")
        ingredient_formset = IngredientsFormSet(prefix="ingredient_formset")

    return render(request, 'recipes/ingredient-group.html', {
        'ingredient_group_form': ingredient_group_form,
        'ingredient_formset': ingredient_formset,
        'measurements': Ingredients.MEASUREMENT_CHOICES,
        'recipe': recipe,
        'edit_html': False,
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
    messages.success(request, f'Recipe "{recipe.name}" has been successfully deleted!')
    return redirect('recipes-home')

def delete_ingredient_group(request, recipe_id, ingredient_group_id):
    """
    Deletes an individual ingredient group for the recipe from the database,
    as long as there is at least one or more ingredient groups for the recipe.

    :param request:
    :param recipe_id: The id of the recipe the ingredient group is associated with
    :param ingredient_group_id: the id of the ingredient group user wishes to delete
    :return:
    """

    recipe = get_object_or_404(Recipes, id=recipe_id)
    ingredient_group = get_object_or_404(IngredientGroup, id=ingredient_group_id)
    number_of_ingredient_groups = len(recipe.ingredient_groups.all())
    if number_of_ingredient_groups > 1:
        ingredient_group.delete()
        messages.success(request, f'Ingredient Group "{ingredient_group.name}" has been successfully deleted!')
        return redirect('recipe-details', recipe_id=recipe_id)
    else:
        messages.error(request, 'Operation cancelled! A recipe needs at lest one ingredient group.')
    return redirect('recipe-details', recipe_id=recipe_id)