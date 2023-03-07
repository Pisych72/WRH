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
      'title': forms.TextInput(attrs={'class':'form-control','style':'width:955px;','id':'idtitle'}),
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
      'title': forms.TextInput(attrs={'class':'form-control','style':'width:955px;','id':'idtitle'}),
      }

class PostavForm(forms.ModelForm):
   class Meta:
      model = Postav
      fields = ['title']
      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','style':'width:955px;','id':'idtitle'}),
      }

class SpisForm(forms.ModelForm):
   class Meta:
      model = Spis
      fields = ['title']
      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','style':'width:955px;','id':'idtitle'}),
      }

class PodrazForm(forms.ModelForm):
   class Meta:
      model = Podraz
      fields = ['title']
      widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control', 'style':'width:955px;','id':'idtitle'}),
         }
class PodrazForm2(forms.ModelForm):
   class Meta:
      model = Podraz
      fields = ['title']
      widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control', 'style':'width:460px;','id':'idtitle2'}),
         }
class FioForm(forms.ModelForm):
   class Meta:
      model = Fio
      fields = ['title']
      widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control', 'style':'width:955px;','id':'idtitle'}),
         }

class ObctForm(forms.ModelForm):
   class Meta:
      model = Obct
      fields = ['title','podraz']
      widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control', 'style':'width:443px;','id':'idtitle'}),
    'podraz': forms.Select(attrs={'class': 'form-control', 'style': 'width:440px;', 'id': 'idpodraz'}),
         }

class NomForm(forms.ModelForm):
   class Meta:
      model = Nom
      fields = '__all__'
      widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:410px;','id':'idtitle'}),
    'izm': forms.Select(attrs={'class': 'form-control', 'style': 'width:100px;margin:0;','id':'idizm'}),
    'category': forms.Select(attrs={'class': 'form-control', 'style': 'width:200px;','id':'idcat'}),
     'srok': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:45px;padding-right:0;margin-left:15px;','id':'idsrok'}),
         }


class UnitForm2(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:460px;', 'id': 'idtitle2'}),
        }


class CategoryForm2(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:460px;', 'id': 'idtitle3'}),
        }