from django import forms
from django.forms import inlineformset_factory
from django.forms.models import modelformset_factory

from .models import Recipes, IngredientGroup, Ingredients

IngredientGroupFormSet = inlineformset_factory(
    Recipes,
    IngredientGroup,
    fields=['name'],
    extra=1,
    can_delete=True,
)

class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['ingredient', 'amount', 'measurement']
        widgets = {
            'ingredient': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'measurement': forms.ChoiceField(choices=Ingredients.MEASUREMENT_CHOICES),
        }

IngredientsFormSet = modelformset_factory(
    Ingredients,
    IngredientsForm,
    extra=1,
    can_delete=True,
)