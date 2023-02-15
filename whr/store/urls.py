
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
   path('unit/<str:pk>',UnitUpdate,name='UnitUpdate'),
   path('unitdelete/<str:pk>', UnitDelete, name='UnitDelete'),
   # Справочник категорий
   path('category/', CategoryList, name='CategoryList'),
   path('category/<str:pk>',CategoryUpdate,name='CategoryUpdate'),
   path('categorydelete/<str:pk>', CategoryDelete, name='CategoryDelete'),
# Справочник поставщиков
   path('postav/', PostavList, name='PostavList'),
   path('postav/<str:pk>',PostavUpdate,name='PostavUpdate'),
   path('postavdelete/<str:pk>', PostavDelete, name='PostavDelete'),
# Справочник списания
   path('spis/', SpisList, name='SpisList'),
   path('spis/<str:pk>',SpisUpdate,name='SpisUpdate'),
   path('spisdelete/<str:pk>', SpisDelete, name='SpisDelete'),
# Справочник подразделения
   path('podraz/', PodrazList, name='PodrazList'),
   path('podraz/<str:pk>',PodrazUpdate,name='PodrazUpdate'),
   path('podrazdelete/<str:pk>', PodrazDelete, name='PodrazDelete'),
# Справочник подотчетники
   path('fio/', FioList, name='FioList'),
   path('fio/<str:pk>',FioUpdate,name='FioUpdate'),
   path('fiodelete/<str:pk>', FioDelete, name='FioDelete'),
# Справочник номенклатура
   path('nom/', NomList, name='NomList'),
   path('nom/<str:pk>',NomUpdate,name='NomUpdate'),
   path('nomdelete/<str:pk>', NomDelete, name='NomDelete'),
# Справочник объекты
   path('obct/', ObctList, name='ObctList'),
   path('obct/<str:pk>',ObctUpdate,name='ObctUpdate'),
   path('obctdelete/<str:pk>', ObctDelete, name='ObctDelete'),
]