from django import forms
from django.forms import ModelForm

from .models import TodoModels

class TodoForms(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = TodoModels
        fields = '__all__'