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