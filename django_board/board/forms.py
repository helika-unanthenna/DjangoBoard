from django import forms
from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            'name',
            'age',
            'address',
            'additional_details'
        ]