from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist, ValidationError
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
   'url_delete': reverse('SprDelete'),'url_update':reverse('SprUpdate')})

# 'Справочник категории'
def CategoryList(request):
    unit = Category.objects.all()
    form = CategoryForm()
    return render(request, 'store/spr/SprList.html', {'title': "Категории",
                                                      'unit': unit, 'form': form, 'pic_label': 'Категории',
                                                      'url_name': reverse('SaveCategory'),
                                                      'url_delete': reverse('CatDelete'),
                                                      'url_update': reverse('CatUpdate')
                                                      })
# 'Справочник Поставщики'
def PostavList(request):
    unit = Postav.objects.all()
    form = PostavForm()
    return render(request, 'store/spr/SprList.html', {'title': "Поставщики",
                                                      'unit': unit, 'form': form, 'pic_label': 'Поставщики',
                                                      'url_name': reverse('SavePostav'),
                                                      'url_delete': reverse('PostavDelete'),
                                                      'url_update':reverse('PostavUpdate')})
# 'Справочник Списание'
def SpisList(request):
    unit = Spis.objects.all()
    form = SpisForm()
    return render(request, 'store/spr/SprList.html', {'title': "Списание",
                                                      'unit': unit, 'form': form, 'pic_label': 'Причины списания',
                                                      'url_name': reverse('SaveSpis'),
                                                      'url_delete': reverse('SpisDelete'),
                                                      'url_update':reverse('SpisUpdate')})
# 'Справочник Подразделения'
def PodrazList(request):
    unit = Podraz.objects.all()
    form = PodrazForm()

    return render(request, 'store/spr/SprList.html', {'title': "Подраз.",
                                                      'unit': unit, 'form': form, 'pic_label': 'Подраз.',
                                                      'url_delete': reverse('PodrazDelete'),
                                                      'url_name': reverse('SavePodraz'),
                                                      'url_update': reverse('PodrazUpdate')

                                                      })
# 'Справочник Подотчетники'
def FioList(request):
    unit = Fio.objects.all()
    form = FioForm()
    return render(request, 'store/spr/SprList.html', {'title': "Подотчет.",
                                                      'unit': unit, 'form': form, 'pic_label': 'Подотчет.',
                                                      'url_name': reverse('SaveFio'),
                                                      'url_delete': reverse('FioDelete'),
                                                      'url_update':reverse('FioUpdate')})
# 'Справочник Объекты'
def ObctList(request):
    unit = Obct.objects.all()
    form = ObctForm()
    form2=PodrazForm2()

    return render(request, 'store/spr/SprObct.html', {'title': "Объекты",
                                                      'unit': unit, 'form': form, 'pic_label': 'Объекты',
                                                      'url_name': reverse('SaveObct'),
                                                      'url_delete': reverse('ObctDelete'),
                                                      'url_name2': reverse('SavePodraz2'),
                                                      'form2': form2,'url_update': reverse('ObctUpdate'),
                                                      })


# '****************************************AJAX************************************'
# сохранение на ajax (Единица измерения):
def SprSave(request):
        if request.method=='POST':
            form=UnitForm(request.POST)

        if form.is_valid():
            title=request.POST['title']
            uid = request.POST['unitid']
            if uid=='':
                newrecord = Unit(title=title)
            else:
                newrecord = Unit(title=title,id=uid)

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
            uid = request.POST['unitid']
            if uid == '':
                newrecord = Category(title=title)
            else:
                newrecord = Category(title=title, id=uid)
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
            uid = request.POST['unitid']
            if uid == '':
                newrecord = Postav(title=title)
            else:
                newrecord = Postav(title=title, id=uid)
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
            uid = request.POST['unitid']
            if uid == '':
                newrecord = Spis(title=title)
            else:
                newrecord = Spis(title=title, id=uid)
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
            uid = request.POST['unitid']
            if uid == '':
                newrecord = Podraz(title=title)
            else:
                newrecord = Podraz(title=title, id=uid)
            newrecord.save()
            un=Podraz.objects.values()
            unit_data=list(un)
            return JsonResponse({'status':'Save','unit_data':unit_data})
        else:
            return JsonResponse({'status':0})

    # 'сохранение Подразделения2'
def SavePodraz2(request):
    if request.method == 'POST':
        form2 = PodrazForm2(request.POST)
        if form2.is_valid():
            print('YES')
            title = request.POST['title']
            newrecord = Podraz(title=title)
            newrecord.save()
            un = Obct.objects.values('id', 'title', 'podraz__title')
            unit_data = list(un)
            pd=Podraz.objects.values()
            podraz_data=list(pd)
            print(podraz_data)
            return JsonResponse({'status': 'Save', 'unit_data': unit_data,'podraz_data':podraz_data})
        else:
            print('NO')
            return JsonResponse({'status': 0})

#'сохранение Подотчетники'
def SaveFio(request):
    if request.method=='POST':
        form = FioForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            uid = request.POST['unitid']
            if uid == '':
                newrecord = Fio(title=title)
            else:
                newrecord = Fio(title=title, id=uid)
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
        print("Мы тут!")
        if form.is_valid():
            print("Форма валидна")
            uid = request.POST['unitid']
            title = request.POST['title']
            podraz=request.POST['podraz']

            if uid =='':

                newrecord=Obct(title=title,podraz_id=podraz)
            else:

                newrecord = Obct(title=title, podraz_id=podraz,id=uid)
            newrecord.save()
            un=Obct.objects.values('id','title','podraz__title')


            unit_data=list(un)
            print(unit_data)
            return JsonResponse({'status':'Save','unit_data':unit_data})
        else:
            print("Форма не валидна")
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

# Редактирование////////////////////////////////////////////////////////////////
#///////////// Редактирование единицы измерения//////////////////
def SprUpdate(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        unit=Unit.objects.get(pk=id)
        unit_data={'id':unit.id,'title':unit.title}
        print(unit_data)
        return JsonResponse(unit_data)
    else:
        return JsonResponse({'status':0,})

# редактирование категории
def CatUpdate(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        print(id)
        unit=Category.objects.get(pk=id)
        unit_data={'id':unit.id,'title':unit.title}
        print(unit_data)
        return JsonResponse(unit_data)
    else:
        return JsonResponse({'status':0,})

# редактирование поставшика
def PostavUpdate(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        print(id)
        unit=Postav.objects.get(pk=id)
        unit_data={'id':unit.id,'title':unit.title}
        print(unit_data)
        return JsonResponse(unit_data)
    else:
        return JsonResponse({'status':0,})

# редактирование списания
def SpisUpdate(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        print(id)
        unit=Spis.objects.get(pk=id)
        unit_data={'id':unit.id,'title':unit.title}
        print(unit_data)
        return JsonResponse(unit_data)
    else:
        return JsonResponse({'status':0,})

# редактирование подразделения
def PodrazUpdate(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        print(id)
        unit=Podraz.objects.get(pk=id)
        unit_data={'id':unit.id,'title':unit.title}
        print(unit_data)
        return JsonResponse(unit_data)
    else:
        return JsonResponse({'status':0,})

# редактирование подотчета
def FioUpdate(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        print(id)
        unit=Fio.objects.get(pk=id)
        unit_data={'id':unit.id,'title':unit.title}
        print(unit_data)
        return JsonResponse(unit_data)
    else:
        return JsonResponse({'status':0,})


# Номенклатура
#Создание номенклатуры
def SprNom(request):
    form=NomForm()
    unit=Nom.objects.all()
    return render(request,'store/spr/SprNom.html',{'title':"Номенклатура",'form':form,'unit':unit,
    'pic_label': 'Номенкл.', })

# редактирование номенклатуры

def NomSave(request):
    if request.method =='POST':
        form=NomForm(request.POST)

        if form.is_valid():
            print('Form is valid!!!')
            return JsonResponse({'status':'Save'})
        else:
            print('Not valid form')
            return JsonResponse({'status':0})






# Объекты

# редактирование объекта

def ObctUpdate(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        unit=Obct.objects.get(pk=id)
        unit_data={'id':unit.id,'title':unit.title,'podraz':unit.podraz.title,'idpodraz':unit.podraz.id}
        return JsonResponse(unit_data)
    else:
        return JsonResponse({'status':0,})



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