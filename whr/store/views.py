from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.db.models import Sum
from django.contrib import messages
import datetime
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import *
from .models import *
# Create your views here.

def index(request):
   return render(request, 'store/menu.html',{'title':'Центральный склад'} )


def DocMenu(request):
   return render(request,'store/menu/Docs.html',{'title':'Документы'})

def SpravMenu(request):
   return render(request,'store/menu/SpravMenu.html',{'title':'Справочники'})

def ReportMenu(request):
   return render(request,'store/menu/ReportMenu.html',{'title':'Отчеты'})

#Единицы измерения (UnitList)
#def UnitList(request):
#   unit=Unit.objects.all()
#   return render(request,'store/spr/UnitList.html',{'title':"Единицы измерения",'unit':unit})

#Создание единицы измерения
def UnitList(request):
   unit = Unit.objects.all()
   formmessage='Новая единица измерения:'
   if request.method == 'POST':
      form = UnitForm(request.POST)

      if form.is_valid():

         form.save()
         return redirect("UnitList")

   else:

         form=UnitForm()
   return render(request,'store/spr/UnitList.html',{'title':"Единицы измерения",'unit':unit,'form':form,})

# редактирование единицы измерения

def UnitUpdate(request,pk):
     unit=Unit.objects.all()
     current_unit = Unit.objects.get(pk=pk)
     if request.method == 'POST':
         form=UnitForm(request.POST,instance=current_unit)
         if form.is_valid():
           form.save()
           return redirect('UnitList')
     else:
        form=UnitForm(instance=current_unit)
        return render(request,'store/spr/UnitUpdate.html',{'title':"Единицы измерения",'unit':unit,'form':form,})

# удаление единицы измерения:
def UnitDelete(request, pk):
   unit = Unit.objects.all()
   current_unit = Unit.objects.get(pk=pk)
   if request.method == 'POST':
      form = UnitForm(request.POST, instance=current_unit)
      if form.is_valid():
         current_unit.delete()
         return redirect('UnitList')
   else:
      form = UnitForm(instance=current_unit)
      return render(request, 'store/spr/UnitDelete.html', {'title': "Единицы измерения", 'unit': unit, 'form': form, })


# Логин
def loginUser(request):
   if request.method == 'POST':
      form = UserLoginForm(data=request.POST)
      if form.is_valid():
         user = form.get_user()
         login(request, user)
         return redirect('home')
   else:
      form = UserLoginForm()
   return render(request, 'store/loginUser.html', {"form": form})


def UserOut(request):
   logout(request)
   return redirect('loginUser')