from django.shortcuts import render

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
    # TODO add in form logic for adding new recipe with ingredients.
    return render(request, 'recipes/new-recipe.html')

def cookbook(request):
    """
    Opens the webpage showing everything in the cookbook.

    :param request:
    :return:
    """
    return render(request, 'recipes/cookbook.html')