
from django.urls import path
from .views import *

urlpatterns=[
   path('', loginUser, name='loginUser'),
   path('main/',index,name='home'),
   path('out/',UserOut,name='UserOut'),
   path ('docs/',DocMenu,name='DocMenu'),
   path ('sprav/',SpravMenu,name='SpravMenu'),
   path('report/', ReportMenu, name='ReportMenu'),
   # Справочник единиц измерения
   path('unit/', UnitList, name='UnitList'),
   #path('unit/<str:pk>',UnitUpdate,name='UnitUpdate'),
   #path('unitdelete/<str:pk>', UnitDelete, name='UnitDelete'),
   # Справочник категорий
   path('category/', CategoryList, name='CategoryList'),

# Справочник поставщиков
   path('postav/', PostavList, name='PostavList'),


# Справочник списания
   path('spis/', SpisList, name='SpisList'),

# Справочник подразделения
   path('podraz/', PodrazList, name='PodrazList'),

# Справочник подотчетники
   path('fio/', FioList, name='FioList'),

# Справочник номенклатура
   path('SprNom/', SprNom, name='SprNom'),
   path('NomSave/',NomSave,name='NomSave'),

# Справочник объекты
   path('obct/', ObctList, name='ObctList'),


# Обработка ошибки удаления
   path('error/', ErrorDelete, name='ErrorDelete'),
# сохранение данных справочников через AJAX
   path('spr_Save/',SprSave,name='SprSave'),
   path('category_save/',SaveCategory,name='SaveCategory'),
   path('postav_save/',SavePostav,name='SavePostav'),
   path('spis_save/',SaveSpis,name='SaveSpis'),
   path('podraz_save/',SavePodraz,name='SavePodraz'),
   path('fio_save/',SaveFio,name='SaveFio'),
   path('SaveObct/',SaveObct,name='SaveObct'),
   path('podraz_save2/', SavePodraz2, name='SavePodraz2'),

# удаление строк из справочников
   path('SprDelete/',SprDelete,name='SprDelete'),
   path('CatDelete/',CatDelete,name='CatDelete'),
   path('PodrazDelete/',PodrazDelete,name='PodrazDelete'),
   path('FioDelete/',FioDelete,name='FioDelete'),
   path('PostavDelete/',PostavDelete,name='PostavDelete'),
   path('FioDelete/',FioDelete,name='FioDelete'),
   path('SpisDelete/',SpisDelete,name='SpisDelete'),
   path('ObctDelete/',ObctDelete,name='ObctDelete'),
   path('NomDelete/',NomDelete,name='NomDelete'),

# Редактирование справочников
   path('SprUpdate/',SprUpdate,name='SprUpdate'),
   path('CatUpdate/',CatUpdate,name='CatUpdate'),
   path('PodrazUpdate/',PodrazUpdate,name='PodrazUpdate'),
   path('PostavUpdate/',PostavUpdate,name='PostavUpdate'),
   path('FioUpdate/',FioUpdate,name='FioUpdate'),
   path('SpisUpdate/',SpisUpdate,name='SpisUpdate'),
   path('ObctUpdate/',ObctUpdate,name='ObctUpdate'),
   path('NomUpdate/',NomUpdate,name='NomUpdate'),
   path('NomAddUnit/', NomAddUnit, name='NomAddUnit'),
   path('NomAddCat/', NomAddCat, name='NomAddCat'),

#Документы
   path('NewOstDoc/',NewOstDoc,name='NewOstDoc'),
   path('StringOstSave/', StringOstSave, name='StringOstSave'),
   path('JurnalOst/', JurnalOst, name='JurnalOst'),
   path('AddStringOst/<str:pk>',AddStringOst,name='AddStringOst'),
   path('ReturnToJurnalOst/',ReturnToJurnalOst,name='ReturnToJurnalOst'),
   path('EditOstDoc/',EditOstDoc,name='EditOstDoc'),
   path('DeleteOstStringTable/',DeleteOstStringTable,name='DeleteOstStringTable'),
   path('UpdateOstStringTable/',UpdateOstStringTable,name='UpdateOstStringTable'),
   path('DeleteOstDoc/',DeleteOstDoc,name='DeleteOstDoc'),

   # Поступление ТМЦ//////////////////////////////////////////////////////
   path('JurnalPost/',JurnalPost,name='JurnalPost'), #Журнал документов поступление
   path('AddStringPost/<str:pk>',AddStringPost,name='AddStringPost'), #Добавление строк в новый документ
   path('ReturnToJurnalPost/', ReturnToJurnalPost, name='ReturnToJurnalPost'),#сохранение и возврат в журнад
   path('EditPostDoc/',EditPostDoc,name='EditPostDoc'),
   # Добавление номенклатуры из документа
   path('AddNomFromDoc/',AddNomFromDoc,name='AddNomFromDoc'),
# Добавление поставщика из документа
   path('AddPostavFromDoc/',AddPostavFromDoc,name='AddPostavFromDoc',),
# Получене актуальных данных
   path('GetActualData/',GetActualData,name='GetActualData'),
   path('JurnalMove/', JurnalMove, name='JurnalMove'),  # Журнал документов перемещения
   path('FillMoveSelect/',FillMoveSelect,name='FillMoveSelect'), # заполнение селекта объектов
   path('AddStringMove/<str:pk>',AddStringMove,name='AddStringMove'), #табличная часть новый документ перемещение
   path('SaveMoveString/',SaveMoveString,name='SaveMoveString'),
   path('ReturnToJurnalMove/', ReturnToJurnalMove, name='ReturnToJurnalMove'),  # сохранение и возврат в журнад
   path('EditMoveDoc/', EditMoveDoc, name='EditMoveDoc'),
   path('DeleteMoveDoc/', DeleteMoveDoc, name='DeleteMoveDoc'),
   path('DeleteMoveStringTable/',DeleteMoveStringTable,name='DeleteMoveStringTable'),
   path('getDataToModal/',getDataToModal,name='getDataToModal'),
   path('SaveMoveStringTable/',SaveMoveStringTable,name='SaveMoveStringTable'),
   path('PrintMoveDoc/<str:pk>',PrintMoveDoc,name='PrintMoveDoc'),
   # Отчеты
   path('ReportOst/',ReportOst,name='ReportOst'), # Меню отчетов
   path('Kartochka/<str:pk>/<str:price>',Kartochka,name='Kartochka'),
   path('PodrazReport/',PodrazReport,name='PodrazReport'),
   path('GetPodrazData/',GetPodrazData,name='GetPodrazData'),
   path('GetPodrazData2/',GetPodrazData2,name='GetPodrazData2'),
   path('GetObctData/',GetObctData,name='GetObctData'),
   path('GetObctData2/', GetObctData2, name='GetObctData2'),
   path('ObctReport/',ObctReport,name='ObctReport'),
   path('FioReport/',FioReport,name='FioReport'),
   path('GetPodrazData3/', GetPodrazData3, name='GetPodrazData3'),
   path('GetObctData3/', GetObctData3, name='GetObctData3'),


]