"""example

from django import forms
from .models import ColorModel

class ColorModelForm(forms.ModelForm):
    class Meta:
        model= ColorModel
        fields= ["COLOR_CHOICE"]
"""
