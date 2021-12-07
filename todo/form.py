from django import forms
from .models import ToDoApp

class AddForm(forms.ModelForm):
    class Meta:
        model= ToDoApp
        fields=["desc"]
        widgets = {
            'desc': forms.TextInput(attrs={'class': 'desc','placeholder': 'Please add your task.....'}),
        }