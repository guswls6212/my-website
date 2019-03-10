from django.db import models
from django import forms
from django.forms import ModelForm
from leeblog.models import Maker, Label, MultiFileLabel, Recipe, Ingredient, Instruction
from django.forms import ClearableFileInput

from django.forms.models import inlineformset_factory

# from leeblog.models import Recipe, Ingredient, Instruction


class MakerForm(forms.ModelForm):

    class Meta:
        model = Maker
        fields ='__all__'

class LabelForm(forms.ModelForm):

    class Meta:
        model = Label
        fields =[
                    # 'maker',
                    'sw_version',
                    'os_version'
                    # 'label_file'
        ]

# MultiFileLabelFormSet = inlineformset_factory(Label,
#                                             MultiFileLabel,
#                                             form=LabelForm(),
#                                             extra=1,
#                                             widgets={'label_file': ClearableFileInput(attrs={'multiple': True}),})
#
#
# class MultiFileLabelForm(forms.ModelForm):
#     class Meta:
#         model = MultiFileLabel
#         fields = ['label_file']
#         widgets = {
#             'label_file': ClearableFileInput(attrs={'multiple': True}),
#         }



class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

IngredientFormSet = inlineformset_factory(Recipe, Ingredient, form=RecipeForm, extra=1)
InstructionFormSet = inlineformset_factory(Recipe, Instruction, form=RecipeForm, extra=2, fields=['number'])
