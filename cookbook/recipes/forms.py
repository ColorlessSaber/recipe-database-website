from django import forms
from django.forms import inlineformset_factory
from django.forms.models import modelformset_factory

from .models import Recipes, IngredientGroup, Ingredients

class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=Recipes.CATEGORY_CHOICES),
            'time_min': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
            'time_max': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
            'serving': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }

class IngredientGroupForm(forms.ModelForm):
    class Meta:
        model = IngredientGroup
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['ingredient', 'amount', 'measurement']
        widgets = {
            'ingredient': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'measurement': forms.ChoiceField(choices=Ingredients.MEASUREMENT_CHOICES),
        }

IngredientsFormSet = inlineformset_factory(
    IngredientGroup,
    Ingredients,
    form=IngredientsForm,
    extra=1,
    can_delete=True,
)