from django import forms
from django.forms import ModelForm
from .models import Todo

class NewTodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
