from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Username'
        }
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Password'
        }
    ))
    class Meta:
        model = CustomUser
        fields = ['username','password']

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Input Username'
            }
    ))
    email = forms.CharField(label='Email', widget=forms.TextInput(
            attrs={
               'class' : 'form-control',
                'placeholder' : 'Input Email'
            }
    ))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Password'
        }
    ))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Confirm Password'
        }
    ))

    class Meta:
        model = CustomUser
        fields = ['username','email','password1','password2']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['Name','Age','Gender','Height','Weight']
#  Name, Age, Gender, Height, Weight   input daily consumed calories (Item name, Calorie consumed) 
class CalorieInfoForm(forms.ModelForm):
    class Meta:
        model = CalorieInfo
        fields = ['Item_Name','Calorie_Consumed']
