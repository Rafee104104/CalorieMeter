from .views import *
from django.urls import path

urlpatterns = [
    path('',registration,name='registration'),
    path('homepage/',homepage,name='homepage'),
    path('userlogin/',userlogin,name='userlogin'),
    path('editCalorieInfo/',editCalorieInfo,name='editCalorieInfo'),
    path('editUserInfo/',editUserInfo,name='editUserInfo'),
    path('userInfo/',userInfo,name='userInfo'),
    path('calorieInfo/',calorieInfo,name='calorieInfo'),
    path('user_logout/',user_logout,name='user_logout')
]