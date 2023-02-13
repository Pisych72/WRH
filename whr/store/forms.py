from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',widget=forms.TextInput(attrs={'class':'form-control loginform'}))
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class':'form-control loginform' }))

class UnitForm(forms.ModelForm):
   class Meta:
      model = Unit
      fields = ['title']

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','style':'width:822px'}),
      }

   def __init__(self, *args, **kwargs):
       super(UnitForm, self).__init__(*args, **kwargs)
       self.fields['title'].label = ""