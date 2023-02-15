from django import forms
from .models import Add , Category

class AddForm(forms.ModelForm):
  class Meta:
    model = Add
    fields = [
      'author' , 
      'moveName',
      'moveImage',
      'movesumarize',
      'viewers',
      'rating',
      'date',
      'category',
    ]
    widgets = {
      'author' : forms.TextInput(attrs={'class' : 'input'}),
      'moveName' : forms.TextInput(attrs={'class' : 'input'}),
      'moveImage' : forms.FileInput(attrs={'class' : 'input'}),
      'movesumarize' : forms.TextInput(attrs={'class' : 'input'}),
      'viewers' : forms.NumberInput(attrs={'class' : 'input'}),
      'rating' : forms.NumberInput(attrs={'class' : 'input'}),
      'date' : forms.DateInput(attrs={'class' : 'input'}),
      'category' : forms.Select(attrs={'class' : 'input'}),
    }