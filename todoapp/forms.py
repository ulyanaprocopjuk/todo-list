from django import forms
from django.forms import ModelForm

from .models import Tasks

class AddTaskForm(forms.ModelForm):
    task = forms.CharField(max_length = 50, widget = forms.TextInput(attrs = {
                                    'class' : 'form-control',
                                    'placeholder' : 'enter your task..', }))

    class Meta:
        model = Tasks
        fields = '__all__'