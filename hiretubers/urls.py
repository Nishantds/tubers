from django.urls import path
from .import views

urlpatterns=[
    path('hiretuber',views.hiretubers,name='hiretubers'),
   

]