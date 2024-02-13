from django import forms
from .models import *


class AddStreetTypeForm(forms.ModelForm):
    class Meta:
        model = StreetType
        # fields = '__all__'
        fields = ['streettype_name']
        # widgets = {
        #     'streettype_name': forms.TextInput(attrs={'class': 'form-input'})
        # }
