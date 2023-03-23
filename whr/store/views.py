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
import math

def ceil(number, digits) -> float: return math.ceil((10.0 ** digits) * number) / (10.0 ** digits)
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
            title = request.POST['title']
            newrecord = Podraz(title=title)
            newrecord.save()
            un = Obct.objects.values('id', 'title', 'podraz__title')
            unit_data = list(un)
            pd=Podraz.objects.values()
            podraz_data=list(pd)
            return JsonResponse({'status': 'Save', 'unit_data': unit_data,'podraz_data':podraz_data})
        else:
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
        unit=Spis.objects.get(pk=id)
        unit_data={'id':unit.id,'title':unit.title}
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
    form2=UnitForm2()
    form3=CategoryForm2()
    unit=Nom.objects.all()
    return render(request,'store/spr/SprNom.html',{'title':"Номенклатура",'form':form,'unit':unit,
    'pic_label': 'Номенкл.','form2':form2,'form3':form3 })

# редактирование номенклатуры
def NomSave(request):
    if request.method =='POST':
        form=NomForm(request.POST)
        print(request.POST)
        if form.is_valid():
            uid=request.POST['unitid']
            title=request.POST['title']
            izm=Unit.objects.get(pk=request.POST['izm'])
            category = Category.objects.get(pk=request.POST['category'])
            srok = request.POST['srok']
            if uid=='':
                newrecord=Nom(title=title,izm=izm,category=category,srok=srok)
            else:
                print(uid)
                newrecord = Nom.objects.get(pk=uid)
                newrecord.title=title
                newrecord.izm=izm
                newrecord.category=category
                newrecord.srok=srok
            newrecord.save()
            un = Nom.objects.values('id', 'title', 'izm__title','category__title','srok')
            unit_data = list(un)
            print(unit_data)
            print('ok')
            return JsonResponse({'status':'Save','unit_data':unit_data})
        else:
            print('notvalid')
            return JsonResponse({'status':0})
#Удаление номенклатуры
def NomDelete(request):
    if request.method == 'GET':
        id=request.GET.get('sid')
        pi=Nom.objects.get(pk=id)
        try:
            pi.delete()
            return JsonResponse({'status': 'Del', })
        except ProtectedError:
            return JsonResponse({'status': 0, })
    else:
        return JsonResponse({'status':0,})
# редактирование объекта

def NomUpdate(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        unit=Nom.objects.get(pk=id)
        unit_data={'id':unit.id,'title':unit.title,'cat':unit.category.title,'idcat':unit.category.id,
                   'izm':unit.izm.title,'idizm':unit.izm.id,'srok':unit.srok}
        print(unit_data)
        return JsonResponse(unit_data)
    else:
        return JsonResponse({'status':0,})
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
def NomAddUnit(request):
    if request.method=='POST':
        title=request.POST.get('title')
        newrecord=Unit(title=title)
        try:
            newrecord.save()
            un=Unit.objects.values('id','title')
            unit_data = list(un)
            return JsonResponse({'unit_data':unit_data,'status':1})
        except:
            return JsonResponse({'status':0})
#подбор единицы категории из модального окна
def NomAddCat(request):
    if request.method=='POST':
        form=CategoryForm2(request.POST)
        #title=request.POST.get('title')
        #newrecord=Category(title=title)
        try:
            form.save()
            un=Category.objects.values('id','title')
            unit_data = list(un)
            return JsonResponse({'unit_data':unit_data,'status':1})
        except:
            return JsonResponse({'status':0})

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

def NewOstDoc(request):
    podraz=Podraz.objects.get(pk=74)
    postav=Postav.objects.get(pk=9)
    obct=Obct.objects.get(pk=180)
    fio=Fio.objects.get(pk=5)
    form=DocForm(initial={'podraz':podraz,'postav':postav,'obct':obct,'fio':fio})
    form2=JurnalForm()
    return render(request,'store/Doc/DocOst.html',{'form':form,'form2':form2,'pic_label':'Начальные остатки'})

def JurnalOst(request):
    podraz = Podraz.objects.get(pk=74)
    postav = Postav.objects.get(pk=9)
    obct = Obct.objects.get(pk=180)
    fio = Fio.objects.get(pk=5)
    jurnalost=Jurnal.objects.filter(oper=1).order_by('-created_at')
    if request.method=='POST':
        nomerdoc1=request.POST['nomerdoc']
        datadoc1=request.POST['datadoc']
        print(nomerdoc1,datadoc1)
        newost=Jurnal()
        newost.nomerdoc=nomerdoc1
        newost.datadoc=datadoc1
        newost.podraz=podraz
        newost.postav=postav
        newost.obct=obct
        newost.fio=fio
        newost.oper=1
        newost.save()
        un = Jurnal.objects.filter(oper=1).values()
        unit_data=list(un)
        print(newost.id)
        ur=reverse('AddStringOst',args=[newost.id])
        print(ur)
        return JsonResponse({'status':1,'unit_data':unit_data,'url': ur})
    else:
        form=OstDocForm(initial={'podraz':podraz,'postav':postav,'obct':obct,'fio':fio})
    return render(request,'store/Doc/JurnalOst.html',{'jurnalost':jurnalost,'pic_label':'Начальные остатки','form':form,'title':'Журнал начальных остатков'})

def AddStringOst(request,pk):
    doc=Jurnal.objects.get(pk=pk)
    item=JurnalDoc.objects.filter(iddoc=pk)
    nom=Nom.objects.all()
    sum = JurnalDoc.objects.filter(iddoc=pk).aggregate(Sum("summa"))
    sumnds = JurnalDoc.objects.filter(iddoc=pk).aggregate(Sum("summawithnds"))
    if item:
        summa1 = round(sum['summa__sum'], 2)
        summa2 = round(sumnds['summawithnds__sum'], 2)
    else:
        summa1=0.0
        summa2=0.0
    t="Документ № " + doc.nomerdoc +" от "+doc.datadoc.strftime("%d.%m.%Y")
    return render(request,'store/Doc/AddStringOst.html',{'docost':doc,'nom':nom,'title':t,'pic_label':'Начальные остатки','items':item,'s':summa1,'s2':summa2})

def StringOstSave(request):
    podraz = Podraz.objects.get(pk=74)
    postav = Postav.objects.get(pk=9)
    obct = Obct.objects.get(pk=180)
    fio = Fio.objects.get(pk=5)
    jurnalost = Jurnal.objects.filter(oper=1)
    if request.method=='POST':
        idstring=request.POST['idstring']
        iddoc=Jurnal.objects.get(pk=request.POST['id'])
        title=Nom.objects.get(pk=request.POST['title'])
        kol=request.POST['kol']
        price=request.POST['price']
        summa=request.POST['summa']
        nds=request.POST['nds']
        total=request.POST['total']
        if idstring=='':
            print('equel 0')
            newost=JurnalDoc()
        else:
            newost=JurnalDoc.objects.filter(pr=idstring)
            print('no 0')
        newost.iddoc=iddoc
        newost.title=title
        newost.price=price
        newost.summa=summa
        newost.kol=kol
        newost.summawithnds=total
        newost.nds=nds
        newost.podraz=podraz
        newost.postav=postav
        newost.obct=obct
        newost.fio=fio
        newost.oper=1
        newost.uniqfield=(str(newost.title.id)+'_'+str(newost.price))
        newost.save()
        un=JurnalDoc.objects.order_by('title_id').filter(pk=newost.id).values('id','title__title','title__izm__title','price','kol',
                                      'summa','nds','summawithnds','iddoc')

        sum = JurnalDoc.objects.filter(iddoc=iddoc).aggregate(Sum("summa"))
        sumnds = JurnalDoc.objects.filter(iddoc=iddoc).aggregate(Sum("summawithnds"))
        s=(sum['summa__sum'])
        snds=(sumnds['summawithnds__sum'])
        roundsumma=round(s, 2)
        roundnds=round(snds,2)
        unit_data = list(un)
        return JsonResponse({'status': 1, 'unit_data': unit_data,'total':roundsumma,'total_nds':roundnds})

def ReturnToJurnalOst(request):
    if request.method=='POST':
        items=JurnalDoc.objects.filter(iddoc=request.POST['id'])
        if items:
            sum = items.aggregate(Sum("summa"))
            sumnds=items.aggregate(Sum("summawithnds"))
        else:
            sum=0.0
            sumnds=0.0
        doc=Jurnal.objects.get(pk=request.POST['id'])
        doc.nomerdoc=request.POST['nomer']
        doc.datadoc = request.POST['data']
        if items:
            doc.summa=round(sum['summa__sum'],2)
            doc.summawithnds=round(sumnds['summawithnds__sum'],2)
        else:
            doc.summa = 0.0
            doc.summawithnds = 0.0
        doc.save()
        url = reverse('JurnalOst')
        return JsonResponse({'status':1,'url':url})
def EditOstDoc(request):
    if request.method=='POST':
        id=request.POST['id']
        ost=Jurnal.objects.get(pk=id)
        items=JurnalDoc.objects.filter(iddoc=ost.id).values()
        un = Jurnal.objects.values()
        unit_data = list(items)
        ur = reverse('AddStringOst', args=[ost.id])
        return JsonResponse({'status': 1,'url': ur,'unit_data':unit_data})

# удаление строки из таблицы документв Начальные остатки
def DeleteOstStringTable(request):
    if request.method=='POST':
        string=JurnalDoc.objects.get(pk=request.POST['id'])
        string.delete()
        return JsonResponse({'status':1})
# обновление строки таблицы документа Начальные остатки
def UpdateOstStringTable(request):
    item=JurnalDoc.objects.filter(pk=request.POST['id']).values()
    unit_data=list(item)
    print(unit_data)
    price = (unit_data[0]['price'])
    id = (unit_data[0]['id'])
    iddoc_id = (unit_data[0]['iddoc_id'])
    kol = (unit_data[0]['kol'])
    title_id=(unit_data[0]['title_id'])
    summa = (unit_data[0]['summa'])
    summawithnds = (unit_data[0]['summawithnds'])
    nds=(unit_data[0]['nds'])
    d=JurnalDoc.objects.filter(pk=request.POST['id'])
    d.delete()
    return JsonResponse({'price':price,'id':id,'iddoc_id':iddoc_id,'kol':kol,'title_id':title_id,
                         'summa':summa,'summawithnds':summawithnds,'nds':nds})

# Удаление документов остатков
def DeleteOstDoc(request):
    if request.method=='GET':
        print(request.GET['id'])
        item=Jurnal.objects.filter(pk=request.GET['id'])
        try:
            item.delete()
            return JsonResponse({'status': 1, })
        except ProtectedError:
            return JsonResponse({'status': 0, })

#////////////////////////////ПОСТУПЛЕНИЕ НА СКЛАД////////////////////////////////////////////////
#////////////////////////////Журнал документов поступления (oper=2)//////////////////////////////
#////////////////////////////Шаблон - JurnalPost.html ///////////////////////////////////////////
def JurnalPost(request):
    postav=Postav.objects.all()
    jurnalpost=Jurnal.objects.filter(oper=2).order_by('-created_at')
    obct = Obct.objects.get(pk=180)
    fio = Fio.objects.get(pk=5)
    podraz = Podraz.objects.get(pk=74)
    if request.method=='POST':
        postdoc=Jurnal()
        postdoc.oper=2
        postdoc.nomerdoc=request.POST['nomerdoc']
        postdoc.datadoc=request.POST['datadoc']
        postav_item=Postav.objects.get(pk=request.POST['postav'])
        postdoc.postav=postav_item
        postdoc.fio=fio
        postdoc.obct=obct
        postdoc.podraz=podraz
        postdoc.save()
        un = Jurnal.objects.filter(oper=2).values()
        unit_data = list(un)
        print(postdoc.id)
        ur = reverse('AddStringPost', args=[postdoc.id])
        print(ur)
        return JsonResponse({'status': 1, 'unit_data': unit_data, 'url': ur})
    return render(request,'store/Doc/JurnalPost.html',{'postav':postav,'jurnalpost':jurnalpost,'pic_label':'Поступление','title':'Журнал приходных документов'})

# Добавление строк в новый документ поступление
def AddStringPost(request,pk):
    doc = Jurnal.objects.get(pk=pk)
    postav=Postav.objects.get(pk=doc.postav_id)
    item = JurnalDoc.objects.filter(iddoc=pk)
    print(postav)
    postav_list=Postav.objects.all()
    nom = Nom.objects.all()
    sum = JurnalDoc.objects.filter(iddoc=pk).aggregate(Sum("summa"))
    sumnds = JurnalDoc.objects.filter(iddoc=pk).aggregate(Sum("summawithnds"))
    if item:
        summa1 = round(sum['summa__sum'], 2)
        summa2 = round(sumnds['summawithnds__sum'], 2)
    else:
        summa1 = 0.0
        summa2 = 0.0
    t = "Документ № " + doc.nomerdoc + " от " + doc.datadoc.strftime("%d.%m.%Y")
    return render(request, 'store/Doc/AddStringPost.html',
                  {'docost': doc, 'nom': nom, 'title': t, 'pic_label': 'Начальные остатки', 'items': item, 's': summa1,
                   's2': summa2,'postav':postav,'postav_list':postav_list})


def ReturnToJurnalPost(request):
    if request.method == 'POST':
        items = JurnalDoc.objects.filter(iddoc=request.POST['id'])
        if items:
            sum = items.aggregate(Sum("summa"))
            sumnds = items.aggregate(Sum("summawithnds"))
        else:
            sum = 0.0
            sumnds = 0.0
        doc = Jurnal.objects.get(pk=request.POST['id'])
        postav=Postav.objects.get(pk=request.POST['postav'])
        doc.nomerdoc = request.POST['nomer']
        doc.datadoc = request.POST['data']
        doc.postav=postav
        if items:
            doc.summa = round(sum['summa__sum'], 2)
            doc.summawithnds = round(sumnds['summawithnds__sum'], 2)
        else:
            doc.summa = 0.0
            doc.summawithnds = 0.0
        doc.save()
        url = reverse('JurnalPost')
        return JsonResponse({'status': 1, 'url': url})
def EditPostDoc(request):
    if request.method=='POST':
        id=request.POST['id']
        ost=Jurnal.objects.get(pk=id)
        items=JurnalDoc.objects.filter(iddoc=ost.id).values()
        un = Jurnal.objects.values()
        unit_data = list(items)
        ur = reverse('AddStringPost', args=[ost.id])
        return JsonResponse({'status': 1,'url': ur,'unit_data':unit_data})