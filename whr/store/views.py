from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.db.models import Sum, ProtectedError
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

# Обработка ошибки удаления
def ErrorDelete(request):
    return render(request,'store/spr/ErrorDelete.html',{'title':'Ошибка удаления'})


#Создание единицы измерения
def UnitList(request):
   unit = Unit.objects.all()
   if request.method == 'POST':
      form = UnitForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("UnitList")
   else:
         form=UnitForm()
   return render(request,'store/spr/SprList.html',{'title':"Единицы измерения",'unit':unit,'form':form,
                     'btn_caption': 'Добавить', 'brd_class': 'border-secondary',
                     'btn_class':'btn-primary','pic_label': 'Единицы измерения',
                     'base_url':'UnitList','update_url':'UnitUpdate','delete_url':'UnitDelete'})
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
        return render(request,'store/spr/SprList.html',{'title':"Единицы измерения",'unit':unit,'form':form,
                     'btn_caption': 'Изменить', 'brd_class': 'border-secondary',
                     'btn_class':'btn-primary','pic_label': 'Единицы измерения',
                     'base_url': 'UnitList', 'update_url': 'UnitUpdate',
                     'delete_url': 'UnitDelete'})
# удаление единицы измерения:
def UnitDelete(request, pk):
   unit = Unit.objects.all()
   current_unit = Unit.objects.get(pk=pk)
   if request.method == 'POST':
      form = UnitForm(request.POST, instance=current_unit)
      if form.is_valid():
            try:
                current_unit.delete()
                return redirect('UnitList')
            except ProtectedError:
                return redirect('ErrorDelete')


   else:
      form = UnitForm(instance=current_unit)
      return render(request,'store/spr/SprList.html',{'title':"Единицы измерения",'unit':unit,'form':form,
                     'btn_caption': 'Удалить', 'brd_class': 'border-danger',
                     'btn_class':'btn-danger','pic_label': 'Единицы измерения',
                     'base_url':'UnitList', 'update_url': 'UnitUpdate',
                     'delete_url': 'UnitDelete'})
# Категории
#Создание категории
def CategoryList(request):
   unit = Category.objects.all()
   if request.method == 'POST':
      form = CategoryForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("CategoryList")
   else:
         form=CategoryForm()
   return render(request,'store/spr/SprList.html',{'title':"Категории",'unit':unit,'form':form,
                     'btn_caption': 'Добавить', 'brd_class': 'border-secondary',
                     'btn_class':'btn-primary','pic_label': 'Категории',
                     'base_url': 'CategoryList', 'update_url': 'CategoryUpdate',
                     'delete_url': 'CategoryDelete'})
# редактирование категории

def CategoryUpdate(request,pk):
     unit=Category.objects.all()
     current_unit = Category.objects.get(pk=pk)
     if request.method == 'POST':
         form=CategoryForm(request.POST,instance=current_unit)
         if form.is_valid():
           form.save()
           return redirect('CategoryList')
     else:
        form=CategoryForm(instance=current_unit)
        return render(request,'store/spr/SprList.html',{'title':"Категории",'unit':unit,'form':form,
                     'btn_caption': 'Изменить', 'brd_class': 'border-secondary',
                     'btn_class':'btn-primary','pic_label': 'Категории',
                      'base_url': 'CategoryList', 'update_url': 'CategoryUpdate',
                      'delete_url': 'CategoryDelete'})
# удаление категории:
def CategoryDelete(request, pk):
   unit = Category.objects.all()
   current_unit = Category.objects.get(pk=pk)
   if request.method == 'POST':
      form = CategoryForm(request.POST, instance=current_unit)
      if form.is_valid():
          try:
              current_unit.delete()
              return redirect('CategoryList')
          except ProtectedError:
              return redirect('ErrorDelete')
   else:
      form = CategoryForm(instance=current_unit)
      return render(request,'store/spr/SprList.html',{'title':"Категории",'unit':unit,'form':form,
                     'btn_caption': 'Удалить', 'brd_class': 'border-danger',
                     'btn_class':'btn-danger','pic_label': 'Категории',
                     'base_url': 'CategoryList', 'update_url': 'CategoryUpdate',
                     'delete_url': 'CategoryDelete'})
# Поставшики
#Создание поставщика
def PostavList(request):
   unit = Postav.objects.all()
   if request.method == 'POST':
      form = PostavForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("PostavList")
   else:
         form=PostavForm()
   return render(request,'store/spr/SprList.html',{'title':"Поставщики",'unit':unit,'form':form,
                     'btn_caption': 'Добавить', 'brd_class': 'border-secondary',
                     'btn_class':'btn-primary','pic_label': 'Поставщики',
                     'base_url': 'PostavList', 'update_url': 'PostavUpdate',
                     'delete_url': 'PostavDelete'})
# редактирование поставшика

def PostavUpdate(request,pk):
     unit=Postav.objects.all()
     current_unit = Postav.objects.get(pk=pk)
     if request.method == 'POST':
         form=PostavForm(request.POST,instance=current_unit)
         if form.is_valid():
           form.save()
           return redirect('PostavList')
     else:
        form=PostavForm(instance=current_unit)
        return render(request,'store/spr/SprList.html',{'title':"Поставщики",'unit':unit,'form':form,
                     'btn_caption': 'Изменить', 'brd_class': 'border-secondary',
                     'btn_class':'btn-primary','pic_label': 'Поставщики',
                     'base_url': 'PostavList', 'update_url': 'PostavUpdate',
                     'delete_url': 'PostavDelete'})
# удаление поставшика:
def PostavDelete(request, pk):
   unit = Postav.objects.all()
   current_unit = Postav.objects.get(pk=pk)
   if request.method == 'POST':
      form = PostavForm(request.POST, instance=current_unit)
      if form.is_valid():
          try:
              current_unit.delete()
              return redirect('PostavList')
          except ProtectedError:
              return redirect('ErrorDelete')
   else:
      form = PostavForm(instance=current_unit)
      return render(request,'store/spr/SprList.html',{'title':"Поставщики",'unit':unit,'form':form,
                     'btn_caption': 'Удалить', 'brd_class': 'border-danger',
                     'btn_class':'btn-danger','pic_label': 'Поставщики',
                     'base_url': 'PostavList', 'update_url': 'PostavUpdate',
                     'delete_url': 'PostavDelete'})
# Списание
#Создание списания
def SpisList(request):
   unit = Spis.objects.all()
   if request.method == 'POST':
      form = SpisForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("SpisList")
   else:
         form=SpisForm()
   return render(request,'store/spr/SprList.html',{'title':"Списание",'unit':unit,'form':form,
                     'btn_caption': 'Добавить', 'brd_class': 'border-secondary',
                     'btn_class':'btn-primary','pic_label': 'Списание',
                     'base_url': 'SpisList', 'update_url': 'SpisUpdate',
                     'delete_url': 'SpisDelete'})
# редактирование списания

def SpisUpdate(request,pk):
     unit=Spis.objects.all()
     current_unit = Spis.objects.get(pk=pk)
     if request.method == 'POST':
         form=SpisForm(request.POST,instance=current_unit)
         if form.is_valid():
           form.save()
           return redirect('SpisList')
     else:
        form=SpisForm(instance=current_unit)
        return render(request,'store/spr/SprList.html',{'title':"Списание",'unit':unit,'form':form,
                     'btn_caption': 'Изменить', 'brd_class': 'border-secondary',
                     'btn_class':'btn-primary','pic_label': 'Списание',
                     'base_url': 'SpisList', 'update_url': 'SpisUpdate',
                     'delete_url': 'SpisDelete'})
# удаление списания:
def SpisDelete(request, pk):
   unit = Spis.objects.all()
   current_unit = Spis.objects.get(pk=pk)
   if request.method == 'POST':
      form = SpisForm(request.POST, instance=current_unit)
      if form.is_valid():
          try:
              current_unit.delete()
              return redirect('SpisList')
          except ProtectedError:
              return redirect('ErrorDelete')
   else:
      form = SpisForm(instance=current_unit)
      return render(request,'store/spr/SprList.html',{'title':"Списание",'unit':unit,'form':form,
                     'btn_caption': 'Удалить', 'brd_class': 'border-danger',
                     'btn_class':'btn-danger','pic_label': 'Списание',
                     'base_url': 'SpisList', 'update_url': 'SpisUpdate',
                     'delete_url': 'SpisDelete'})
# Подразделения
#Создание подразделения
def PodrazList(request):
   unit = Podraz.objects.all()
   if request.method == 'POST':
      form = PodrazForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("PodrazList")
   else:
         form=PodrazForm()
   return render(request,'store/spr/SprList.html',{'title':"Подразделения",'unit':unit,'form':form,
                     'btn_caption': 'Добавить', 'brd_class': 'border-secondary',
                     'btn_class':'btn-primary','pic_label': 'Подраздел.',
                     'base_url': 'PodrazList', 'update_url': 'PodrazUpdate',
                     'delete_url': 'PodrazDelete'})
# редактирование подразделения

def PodrazUpdate(request,pk):
     unit=Podraz.objects.all()
     current_unit = Podraz.objects.get(pk=pk)
     if request.method == 'POST':
         form=PodrazForm(request.POST,instance=current_unit)
         if form.is_valid():
           form.save()
           return redirect('PodrazList')
     else:
        form=PodrazForm(instance=current_unit)
        return render(request,'store/spr/SprList.html',{'title':"Подразделения",'unit':unit,'form':form,
                     'btn_caption': 'Изменить', 'brd_class': 'border-secondary',
                     'btn_class':'btn-primary','pic_label': 'Подраздел.',
                     'base_url': 'PodrazList', 'update_url': 'PodrazUpdate',
                     'delete_url': 'PodrazDelete'})
# удаление подразделения:
def PodrazDelete(request, pk):
   unit = Podraz.objects.all()
   current_unit = Podraz.objects.get(pk=pk)
   if request.method == 'POST':
      form = PodrazForm(request.POST, instance=current_unit)
      if form.is_valid():
          try:
              current_unit.delete()
              return redirect('PodrazList')
          except ProtectedError:
              return redirect('ErrorDelete')
   else:
      form = PodrazForm(instance=current_unit)
      return render(request,'store/spr/SprList.html',{'title':"Подразделения",'unit':unit,'form':form,
                     'btn_caption': 'Удалить', 'brd_class': 'border-danger',
                     'btn_class':'btn-danger','pic_label': 'Подраздел.',
                     'base_url': 'PodrazList', 'update_url': 'PodrazUpdate',
                     'delete_url': 'PodrazDelete'})
# Подотчет
#Создание подотчета
def FioList(request):
   unit = Fio.objects.all()
   if request.method == 'POST':
      form = FioForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("FioList")
   else:
         form=FioForm()
   return render(request,'store/spr/SprList.html',{'title':"Подотчет",'unit':unit,'form':form,
                     'btn_caption': 'Добавить', 'brd_class': 'border-secondary',
                     'btn_class':'btn-primary','pic_label': 'Подотчет',
                     'base_url': 'FioList', 'update_url': 'FioUpdate',
                     'delete_url': 'FioDelete'})
# редактирование подотчета

def FioUpdate(request,pk):
     unit=Fio.objects.all()
     current_unit = Fio.objects.get(pk=pk)
     if request.method == 'POST':
         form=FioForm(request.POST,instance=current_unit)
         if form.is_valid():
           form.save()
           return redirect('FioList')
     else:
        form=FioForm(instance=current_unit)
        return render(request,'store/spr/SprList.html',{'title':"Подотчет",'unit':unit,'form':form,
                     'btn_caption': 'Изменить', 'brd_class': 'border-secondary',
                     'btn_class':'btn-primary','pic_label': 'Подотчет',
                     'base_url': 'FioList', 'update_url': 'FioUpdate',
                     'delete_url': 'FioDelete'})
# удаление подотчета:
def FioDelete(request, pk):
   unit = Fio.objects.all()
   current_unit = Fio.objects.get(pk=pk)
   if request.method == 'POST':
      form = FioForm(request.POST, instance=current_unit)
      if form.is_valid():
          try:
              current_unit.delete()
              return redirect('FioList')
          except ProtectedError:
              return redirect('ErrorDelete')
   else:
      form = FioForm(instance=current_unit)
      return render(request,'store/spr/FioList.html',{'title':"Подотчет",'unit':unit,'form':form,
                     'btn_caption': 'Удалить', 'brd_class': 'border-danger',
                     'btn_class':'btn-danger','pic_label': 'Подотчет',
                     'base_url': 'FioList', 'update_url': 'FioUpdate',
                     'delete_url': 'FioDelete'})

# Номенклатура
#Создание номенклатуры
def NomList(request):
   unit=Nom.objects.all()

   if request.method == 'POST':
       form=NomForm(request.POST)
       form2=UnitForm(request.POST)
       print(request.POST)
       if form.is_valid():
           form.save()
           return redirect('NomList')
       if form2.is_valid():
           form2.save()
           return redirect('NomList')
   else:
       form=NomForm()
       form2=UnitForm()
       return render(request,'store/spr/NomList.html',{'title':"Номенклатура",'unit':unit,'form':form,'form2':form2,
   'btn_caption': 'Добавить', 'brd_class': 'border-secondary',
   'btn_class': 'btn-primary', 'pic_label': 'Номенкл.',
   'base_url': 'NomList', 'update_url': 'NomUpdate',
   'delete_url': 'NomDelete'})

# редактирование номенклатуры

def NomUpdate(request,pk):
     unit=Nom.objects.all()
     current_unit = Nom.objects.get(pk=pk)
     if request.method == 'POST':
         form=NomForm(request.POST,instance=current_unit)
         if form.is_valid():
           form.save()
           return redirect('NomList')
     else:
        form=NomForm(instance=current_unit)
        return render(request,'store/spr/NomList.html',{'title':"Номенклатура",'unit':unit,'form':form,
        'btn_caption': 'Изменить', 'brd_class': 'border-secondary',
        'btn_class': 'btn-primary', 'pic_label': 'Номенкл.',
        'base_url': 'NomList', 'update_url': 'NomUpdate',
        'delete_url': 'NomDelete'
                                                          })

# удаление номенклатуры:
def NomDelete(request, pk):
   unit = Nom.objects.all()
   current_unit = Nom.objects.get(pk=pk)
   if request.method == 'POST':
      form = NomForm(request.POST, instance=current_unit)
      if form.is_valid():
          try:
              current_unit.delete()
              return redirect('NomList')
          except ProtectedError:
              return redirect('ErrorDelete')
   else:
      form = NomForm(instance=current_unit)
      return render(request, 'store/spr/NomList.html', {'title': "Номенклатура", 'unit': unit, 'form': form,
      'btn_caption': 'Удалить', 'brd_class': 'border-danger',
      'btn_class': 'btn-danger', 'pic_label': 'Номенкл.',
      'base_url': 'NomList', 'update_url': 'NomUpdate',
      'delete_url': 'NomDelete'
      })

# Объекты
#Создание объекта
def ObctList(request):
   unit = Obct.objects.all()
   if request.method == 'POST':
      form = ObctForm(request.POST)

      if form.is_valid():
         form.save()
         return redirect("ObctList")
   else:
         form=ObctForm()
   return render(request,'store/spr/SprList.html',{'title':"Объекты",
                'unit':unit,'form':form,'btn_caption':'Добавить','brd_class':'border-secondary',
                'btn_class':'btn-primary','pic_label':'Объекты',
                'base_url': 'ObctList', 'update_url': 'ObctUpdate',
                'delete_url': 'ObctDelete'})

# редактирование объекта

def ObctUpdate(request,pk):
     unit=Obct.objects.all()
     current_unit = Obct.objects.get(pk=pk)
     if request.method == 'POST':
         form=ObctForm(request.POST,instance=current_unit)
         if form.is_valid():
           form.save()
           return redirect('ObctList')
     else:
        form=ObctForm(instance=current_unit)
        return render(request,'store/spr/SprList.html',{'title':"Объекты",'unit':unit,'form':form,
                     'btn_caption': 'Изменить', 'brd_class': 'border-secondary',
                     'btn_class':'btn-primary','pic_label': 'Объекты',
                     'base_url': 'ObctList', 'update_url': 'ObctUpdate',
                     'delete_url': 'ObctDelete'})

# удаление объекта:
def ObctDelete(request, pk):
   unit = Obct.objects.all()
   current_unit = Obct.objects.get(pk=pk)
   if request.method == 'POST':
      form = ObctForm(request.POST, instance=current_unit)
      if form.is_valid():
          try:
              current_unit.delete()
              return redirect('ObctList')
          except ProtectedError:
              return redirect('ErrorDelete')
   else:
      form = ObctForm(instance=current_unit)
      return render(request, 'store/spr/SprList.html', {'title': "Объекты", 'unit': unit, 'form': form,
                  'btn_caption': 'Удалить', 'brd_class': 'border-danger',
                  'btn_class':'btn-danger','pic_label': 'Объекты',
                  'base_url': 'ObctList', 'update_url': 'ObctUpdate',
                  'delete_url': 'ObctDelete'})

#подбор единицы измерения из модального окна



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