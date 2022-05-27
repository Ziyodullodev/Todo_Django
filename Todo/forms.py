from django import forms
from django.forms import ModelForm
from django.conf import settings
from .models import TodoModels

class TodoForms(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = TodoModels
        fields = ('__all__')


class UpdateTodo(forms.ModelForm):
    date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Mate:
        model = TodoModels
        fields = ('date',)