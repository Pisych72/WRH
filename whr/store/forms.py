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
      'title': forms.TextInput(attrs={'class':'form-control','style':'width:945px;'}),
      }

class UnitFormSprav(forms.ModelForm):
   class Meta:
      model = Unit
      fields = ['title']
      widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:200px;'}),
      }
   #def __init__(self, *args, **kwargs):
    #   super(UnitForm, self).__init__(*args, **kwargs)
     #  self.fields['title'].label = ""
class CategoryForm(forms.ModelForm):
   class Meta:
      model = Category
      fields = ['title']
      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','style':'width:945px;'}),
      }

class PostavForm(forms.ModelForm):
   class Meta:
      model = Postav
      fields = ['title']
      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','style':'width:945px;'}),
      }

class SpisForm(forms.ModelForm):
   class Meta:
      model = Spis
      fields = ['title']
      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','style':'width:945px;'}),
      }

class PodrazForm(forms.ModelForm):
   class Meta:
      model = Podraz
      fields = ['title']
      widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:945px;'}),
         }

class FioForm(forms.ModelForm):
   class Meta:
      model = Fio
      fields = ['title']
      widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:945px;'}),
         }

class ObctForm(forms.ModelForm):
   class Meta:
      model = Obct
      fields = ['title']
      widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:945px;'}),
         }

class NomForm(forms.ModelForm):
   class Meta:
      model = Nom
      fields = ['title','izm','category','srok']
      widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:420px;'}),
    'izm': forms.Select(attrs={'class': 'form-control', 'style': 'width:150px;margin:0;'}),
    'category': forms.Select(attrs={'class': 'form-control', 'style': 'width:150px;'}),
     'srok': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:45px;padding-right:0'}),
         }