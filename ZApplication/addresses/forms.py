from django import forms
from .models import *


class AddStreetTypeForm(forms.Form):
    streettype_name = forms.CharField(max_length=50)
