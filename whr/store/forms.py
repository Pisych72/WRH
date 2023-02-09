from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',widget=forms.TextInput(attrs={'class':'form-control loginform'}))
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class':'form-control loginform' }))

