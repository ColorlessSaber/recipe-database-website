from django.db import models
# Create your models here.
class Recipes(models.Model):
    """
    database for keeping track of recipes
    """
    CATEGORY_CHOICES = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snack', 'snack'),
        ('dessert', 'dessert'),
        ('dressing', 'dressing'),
        ('other', 'other'),
    )

    name = models.CharField(max_length=255, blank=False, null=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    time_min = models.DecimalField(max_digits=3, decimal_places=0, blank=False, null=False, default=0)
    time_max = models.DecimalField(max_digits=3, decimal_places=0, blank=False, null=False, default=0)
    servings = models.DecimalField(max_digits=3, decimal_places=0, blank=False, null=False, default=0)
    instructions = models.TextField(blank=False, null=False, default='')
    notes = models.TextField(blank=False, null=False, default='')

    objects = models.Manager()

class IngredientGroup(models.Model):
    """
    database for keeping track of ingredient group(s) per recipe.
    An ingredient group is a way to organize groups within the recipe. EX: the dash and the dressing,
    one variation of the dish and a different variation, etc.
    """
    name = models.CharField(max_length=255, blank=False, null=False)
    recipe_ref = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='ingredient_groups')

    objects = models.Manager()

class Ingredients(models.Model):
    """
    database for keeping track of ingredients for each recipe
    """
    MEASUREMENT_CHOICES = (
        ('tsp', 'tsp'),
        ('tbsp', 'tbsp'),
        ('fl oz', 'fl oz'),
        ('cup', 'cup'),
        ('pint', 'pint'),
        ('quart', 'quart'),
        ('oz', 'oz'),
        ('lb', 'lb'),
        ('pinch', 'pinch'),
        ('dash', 'dash'),
        ('scoop', 'scoop'),
        ('ml', 'ml'),
        ('L', 'L'),
        ('g', 'g'),
        ('kg', 'kg'),
        ('can', 'can'),
    )

    group_ref = models.ForeignKey(IngredientGroup, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.CharField(max_length=255, blank=False, null=False, default='') #TODO once website is working, change this to name
    amount = models.CharField(max_length=10, blank=False, null=False, default='')
    measurement = models.CharField(max_length=7, choices=MEASUREMENT_CHOICES)

    objects = models.Manager()
