
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
   path('nom/', NomList, name='NomList'),
   path('nom/<str:pk>',NomUpdate,name='NomUpdate'),
   path('nomdelete/<str:pk>', NomDelete, name='NomDelete'),
# Справочник объекты
   path('obct/', ObctList, name='ObctList'),
   path('obct/<str:pk>',ObctUpdate,name='ObctUpdate'),
   path('obctdelete/<str:pk>', ObctDelete, name='ObctDelete'),
# Обработка ошибки удаления
   path('error/', ErrorDelete, name='ErrorDelete'),
# сохранение данных справочников через AJAX
   path('spr_Save/',SprSave,name='SprSave'),
   path('category_save/',SaveCategory,name='SaveCategory'),
   path('postav_save/',SavePostav,name='SavePostav'),
   path('spis_save/',SaveSpis,name='SaveSpis'),
   path('podraz_save/',SavePodraz,name='SavePodraz'),
   path('fio_save/',SaveFio,name='SaveFio'),
   path('obct_save/',SaveObct,name='SaveObct'),
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

# Редактирование справочников
   path('SprUpdate/',SprUpdate,name='SprUpdate'),
   path('CatUpdate/',CatUpdate,name='CatUpdate'),
   path('PodrazUpdate/',PodrazUpdate,name='PodrazUpdate'),
   path('PostavUpdate/',PostavUpdate,name='PostavUpdate'),
   path('FioUpdate/',FioUpdate,name='FioUpdate'),
   path('SpisUpdate/',SpisUpdate,name='SpisUpdate'),
]