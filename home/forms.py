from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'




class UpgradeTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'