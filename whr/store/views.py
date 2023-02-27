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
from django.http import JsonResponse
import json

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


# 'Справочник единицы измерения'

def UnitList(request):
   unit = Unit.objects.all()
   form=UnitForm()
   return render(request,'store/spr/SprList.html',{'title':"Единицы измерения",
   'unit':unit,'form':form,'pic_label':'Единицы измерения','url_name': reverse('SprSave'),
   'url_delete': reverse('SprDelete'),})

# 'Справочник категории'
def CategoryList(request):
    unit = Category.objects.all()
    form = CategoryForm()
    return render(request, 'store/spr/SprList.html', {'title': "Категории",
                                                      'unit': unit, 'form': form, 'pic_label': 'Категории',
                                                      'url_name': reverse('SaveCategory'),
                                                      'url_delete': reverse('CatDelete'),
                                                      })
# 'Справочник Поставщики'
def PostavList(request):
    unit = Postav.objects.all()
    form = PostavForm()
    return render(request, 'store/spr/SprList.html', {'title': "Поставщики",
                                                      'unit': unit, 'form': form, 'pic_label': 'Поставщики',
                                                      'url_name': reverse('SavePostav'),
                                                      'url_delete': reverse('PostavDelete')})
# 'Справочник Списание'
def SpisList(request):
    unit = Spis.objects.all()
    form = SpisForm()
    return render(request, 'store/spr/SprList.html', {'title': "Списание",
                                                      'unit': unit, 'form': form, 'pic_label': 'Причины списания',
                                                      'url_name': reverse('SaveSpis'),
                                                      'url_delete': reverse('SpisDelete'),  })
# 'Справочник Подразделения'
def PodrazList(request):
    unit = Podraz.objects.all()
    form = PodrazForm()
    return render(request, 'store/spr/SprList.html', {'title': "Подраз.",
                                                      'unit': unit, 'form': form, 'pic_label': 'Подраз.',
                                                      'url_delete': reverse('PodrazDelete'),
                                                      'url_name': reverse('SavePodraz'), })
# 'Справочник Подотчетники'
def FioList(request):
    unit = Fio.objects.all()
    form = FioForm()
    return render(request, 'store/spr/SprList.html', {'title': "Подотчет.",
                                                      'unit': unit, 'form': form, 'pic_label': 'Подотчет.',
                                                      'url_name': reverse('SaveFio'),
                                                      'url_delete': reverse('FioDelete')})
# 'Справочник Объекты'
def ObctList(request):
    unit = Obct.objects.all()
    form = ObctForm()
    return render(request, 'store/spr/SprObct.html', {'title': "Объекты",
                                                      'unit': unit, 'form': form, 'pic_label': 'Объекты',
                                                      'url_name': reverse('SaveObct'),
                                                      'url_delete': reverse('ObctDelete') })

# '****************************************AJAX************************************'
# сохранение на ajax (Единица измерения):
def SprSave(request):
        if request.method=='POST':
            form=UnitForm(request.POST)

        if form.is_valid():
            title=request.POST['title']
            newrecord=Unit(title=title)
            newrecord.save()
            print(newrecord.id,title)
            un=Unit.objects.values()
            unit_data=list(un)
            return JsonResponse({'status':'Save','unit_data':unit_data})
        else:
            return JsonResponse({'status':0})

#'сохранение Категорий'

def SaveCategory(request):
    if request.method=='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            newrecord=Category(title=title)
            newrecord.save()
            un=Category.objects.values()
            unit_data=list(un)
            return JsonResponse({'status':'Save','unit_data':unit_data})
        else:
            return JsonResponse({'status':0})

#'сохранение Поставщика'
def SavePostav(request):
    if request.method=='POST':
        form = PostavForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            newrecord=Postav(title=title)
            newrecord.save()
            un=Postav.objects.values()
            unit_data=list(un)
            return JsonResponse({'status':'Save','unit_data':unit_data})
        else:
            return JsonResponse({'status':0})

#'сохранение Списание'
def SaveSpis(request):
    if request.method=='POST':
        form = SpisForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            newrecord=Spis(title=title)
            newrecord.save()
            un=Spis.objects.values()
            unit_data=list(un)
            return JsonResponse({'status':'Save','unit_data':unit_data})
        else:
            return JsonResponse({'status':0})

#'сохранение Подразделения'
def SavePodraz(request):
    if request.method=='POST':
        form = PodrazForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            newrecord=Podraz(title=title)
            newrecord.save()
            un=Podraz.objects.values()
            unit_data=list(un)
            return JsonResponse({'status':'Save','unit_data':unit_data})
        else:
            return JsonResponse({'status':0})
#'сохранение Подотчетники'
def SaveFio(request):
    if request.method=='POST':
        form = FioForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            newrecord=Fio(title=title)
            newrecord.save()
            un=Fio.objects.values()
            unit_data=list(un)
            return JsonResponse({'status':'Save','unit_data':unit_data})
        else:
            return JsonResponse({'status':0})
#'сохранение Объекты
def SaveObct(request):
    if request.method=='POST':
        form = ObctForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            podraz=request.POST['podraz']
            newrecord=Obct(title=title,podraz_id=podraz)
            newrecord.save()
            un=Obct.objects.values('id','title','podraz__title')


            unit_data=list(un)
            print(unit_data)
            return JsonResponse({'status':'Save','unit_data':unit_data})
        else:
            return JsonResponse({'status':0})

#***********************//AJAX//**********************************************
# удаление единицы измерения
def SprDelete(request):
    if request.method == 'GET':
        id=request.GET.get('sid')
        pi=Unit.objects.get(pk=id)
        try:
            pi.delete()
            return JsonResponse({'status':'Del',})
        except ProtectedError:
            return JsonResponse({'status':0,})
    else:
        return JsonResponse({'status':0,})
# удаление категории
def CatDelete(request):
    if request.method == 'GET':
        id=request.GET.get('sid')
        print(id)
        pi=Category.objects.get(pk=id)
        try:
            pi.delete()
            return JsonResponse({'status': 'Del', })
        except ProtectedError:
            return JsonResponse({'status': 0, })
    else:
        return JsonResponse({'status':0,})
# удаление поставщика
def PostavDelete(request):
    if request.method == 'GET':
        id=request.GET.get('sid')
        pi=Postav.objects.get(pk=id)
        try:
            pi.delete()
            return JsonResponse({'status': 'Del', })
        except ProtectedError:
            return JsonResponse({'status': 0, })
    else:
        return JsonResponse({'status':0,})

# удаление подразделения
def PodrazDelete(request):
    if request.method == 'GET':
        id=request.GET.get('sid')
        pi=Podraz.objects.get(pk=id)
        try:
            pi.delete()
            return JsonResponse({'status': 'Del', })
        except ProtectedError:
            return JsonResponse({'status': 0, })
    else:
        return JsonResponse({'status':0,})

# удаление подотчетника
def FioDelete(request):
    if request.method == 'GET':
        id=request.GET.get('sid')
        pi=Fio.objects.get(pk=id)
        try:
            pi.delete()
            return JsonResponse({'status': 'Del', })
        except ProtectedError:
            return JsonResponse({'status': 0, })
    else:
        return JsonResponse({'status':0,})
# удаление списания
def SpisDelete(request):
    if request.method == 'GET':
        id=request.GET.get('sid')
        pi=Spis.objects.get(pk=id)
        try:
            pi.delete()
            return JsonResponse({'status': 'Del', })
        except ProtectedError:
            return JsonResponse({'status': 0, })
    else:
        return JsonResponse({'status':0,})
#Удаление списания
def ObctDelete(request):
    if request.method == 'GET':
        id=request.GET.get('sid')
        pi=Obct.objects.get(pk=id)
        try:
            pi.delete()
            return JsonResponse({'status': 'Del', })
        except ProtectedError:
            return JsonResponse({'status': 0, })
    else:
        return JsonResponse({'status':0,})






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

# Списание
#Создание списания

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

# Подразделения

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

# Подотчет

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
      'btn_caption': ' Удаление ', 'brd_class': 'border-danger',
      'btn_class': 'btn-danger', 'pic_label': 'Номенкл.',
      'base_url': 'NomList', 'update_url': 'NomUpdate',
      'delete_url': 'NomDelete'
      })

# Объекты

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