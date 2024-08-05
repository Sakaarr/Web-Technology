# myapp/forms.py

from django import forms
from .models import MyFormModel

class MyForm(forms.ModelForm):
    class Meta:
        model = MyFormModel
        fields = ['email', 'example_select', 'example_textarea']
