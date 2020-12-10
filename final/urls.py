
from django.urls import path
from . import views

urlpatterns = [
    path('',views.final, name='final'),
    path('account/',views.account,name='account'),
    path('index/',views.index,name='index'),
    path('createt/',views.createt,name='createt'),
    path('deletet/<str:id>',views.deletet,name='deletet'),
    path('editt/<str:id>',views.editt,name='editt'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('resource/',views.resource,name='resource')
]