from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
   context={'a':5555,'b':'33333',}
   return render(request, 'store/base.html',{'context':context} )