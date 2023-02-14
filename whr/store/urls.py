
from django.urls import path
from .views import *

urlpatterns=[
   path('', loginUser, name='loginUser'),
   path('main/',index,name='home'),
   path('out/',UserOut,name='UserOut'),
   path ('docs/',DocMenu,name='DocMenu'),
   path ('sprav/',SpravMenu,name='SpravMenu'),
   path('report/', ReportMenu, name='ReportMenu'),
   path('unit/', UnitList, name='UnitList'),
   path('unit/<str:pk>',UnitUpdate,name='UnitUpdate'),
   path('unitdelete/<str:pk>', UnitDelete, name='UnitDelete'),
]