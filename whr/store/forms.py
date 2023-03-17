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
class MyDateInput(forms.DateInput):
   input_type = 'date'
   format = '%d-%m-%Y'
class DocForm(forms.ModelForm):
   class Meta:
      model = Jurnal
      fields = ['nomerdoc','datadoc','postav','podraz','fio','obct','summa','nds','summawithnds',
                'oper']
      widgets = {
    'nomerdoc': forms.TextInput(attrs={'class': 'form-control','id':'id_nomerdoc'}),
    'datadoc': MyDateInput(attrs={'id':'id_datadoc'}),
    'postav': forms.Select(attrs={'id':'id_postav','style':"visibility:hidden;"}),
    'podraz': forms.Select(attrs={'id':'id_podraz','style':"visibility:hidden;"}),
    'fio': forms.Select(attrs={'id': 'id_fio','value':5,'style':"visibility:hidden;"}),
    'obct': forms.Select(attrs={'id': 'id_obct','value':180,'style':"visibility:hidden;"}),
    'summa': forms.NumberInput(attrs={'id': 'id_summa','value':0.0}),
    'nds': forms.NumberInput(attrs={'id': 'id_nds','value':20}),
    'summawithnds': forms.NumberInput(attrs={'id': 'id_summawithnds','value':0.0}),
    'oper':forms.NumberInput(attrs={'id':'id_oper','value':1,'style':"visibility:hidden;"})
         }

class JurnalForm(forms.ModelForm):
   class Meta:
      model = JurnalDoc
      fields = ['title','price','summa','nds','summawithnds','oper','iddoc','podraz',
                'postav','obct','fio','spis','uniqfield']
      widgets = {
    'title': forms.Select(attrs={'class': 'form-control','id':'id_title'}),
    'price': forms.NumberInput(attrs={'class':'form-control','id': 'id_price'}),
    'summa': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_summa2'}),
    'nds': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_nds2'}),
    'summawithnds': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_summawithnds2'}),
    'oper':forms.HiddenInput(attrs={'id':'id_oper2'}),
    'iddoc':forms.HiddenInput(attrs={'id':'id_iddoc2'}),
    'podraz': forms.HiddenInput(attrs={'id': 'id_podraz2'}),
    'postav': forms.HiddenInput(attrs={'id': 'id_postav2'}),
    'obct': forms.HiddenInput(attrs={'id': 'id_obct2'}),
    'fio': forms.HiddenInput(attrs={'id': 'id_fio2'}),
    'spis': forms.HiddenInput(attrs={'id': 'id_spis2'}),
    'uniqfield': forms.HiddenInput(attrs={'id': 'id_uniqfield'}),
         }

class OstDocForm(forms.ModelForm):
    class Meta:
        model=Jurnal
        fields = ['nomerdoc', 'datadoc', 'postav', 'podraz', 'fio', 'obct', 'summa', 'nds', 'summawithnds',
                  'oper']
        widgets = {
            'nomerdoc': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_nomerdoc','style':'text-align:right;border-color: grey'}),
            'datadoc': MyDateInput(attrs={'id': 'id_datadoc','style':'height:40px;border-radius:4px;border-color: grey'}),
            'postav': forms.HiddenInput(attrs={'id': 'id_postav','value':9, 'style': "visibility:hidden;"}),
            'podraz': forms.HiddenInput(attrs={'id': 'id_podraz', 'value':74,'style': "visibility:hidden;"}),
            'fio': forms.HiddenInput(attrs={'id': 'id_fio', 'value': 5, 'style': "visibility:hidden;"}),
            'obct': forms.HiddenInput(attrs={'id': 'id_obct', 'value': 180, 'style': "visibility:hidden;"}),
            'summa': forms.HiddenInput(attrs={'id': 'id_summa', 'value': 0.0,'style': "visibility:hidden;"}),
            'nds': forms.HiddenInput(attrs={'id': 'id_nds', 'value': 20,'style': "visibility:hidden;"}),
            'summawithnds': forms.HiddenInput(attrs={'id': 'id_summawithnds', 'value': 0.0,'style': "visibility:hidden;"}),
            'oper': forms.HiddenInput(attrs={'id': 'id_oper', 'value': 1, 'style': "visibility:hidden;"})
        }

class Ost(forms.Form):
    nomerdoc=forms.NumberInput()
    datadoc=MyDateInput()