from .views import *
from django.urls import path

urlpatterns = [
    path('',registration,name='registration'),    
    path('userlogin/',userlogin,name='userlogin'),
    path('editCalorieInfo/',editCalorieInfo,name='editCalorieInfo'),
    path('editUserInfo/',editUserInfo,name='editUserInfo')
]