from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import *
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from datetime import datetime
from django.contrib.auth.models import User

#Project form
class ProjectForm(ModelForm):
    
    class Meta:
        model = Project
        fields = ['user','name','duration','description','avatar']

    def __init__(self, *args, **kwargs):
            user  = kwargs.pop('user', None)
            super(ProjectForm, self).__init__(*args, **kwargs)
            self.fields['user'].initial     = user
            self.fields['user'].widget      = forms.HiddenInput()

            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

#Task form
class TaskForm(ModelForm):
    
    class Meta:
        model = Task
        fields = ['project','name','start_date','end_date','description','assign']

    def __init__(self, *args, **kwargs):
            project  = kwargs.pop('project', None)
            super(TaskForm, self).__init__(*args, **kwargs)
            self.fields['project'].initial     = project
            self.fields['project'].widget      = forms.HiddenInput()
            self.fields['assign'].queryset     =  User.objects.filter(is_staff=False).order_by('username')

            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
    
    def clean(self, *args, **kwargs):
        start_date  = self.cleaned_data.get("start_date")
        end_date    = self.cleaned_data.get("end_date")
        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError("The End Date must be greater than the Start Date.")
        return self.cleaned_data

#Sub Task form
class SubtaskForm(ModelForm):
    
    class Meta:
        model = Subtask
        fields = ['task','name','start_date','end_date','description']

    def __init__(self, *args, **kwargs):
            task  = kwargs.pop('task', None)
            super(SubtaskForm, self).__init__(*args, **kwargs)
            self.fields['task'].initial     = task
            self.fields['task'].widget      = forms.HiddenInput()

            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
    
    def clean(self, *args, **kwargs):
        start_date  = self.cleaned_data.get("start_date")
        end_date    = self.cleaned_data.get("end_date")
        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError("The End Date must be greater than the Start Date.")
        return self.cleaned_data