from django.shortcuts import render, redirect
from django.http import request
from .models import *
from django.contrib.auth import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        height = request.user.userinfo.Height
        weight = request.user.userinfo.Weight
        age = request.user.userinfo.Age
        gender = request.user.userinfo.Gender
        consumed_calorie = request.user.calorieinfo.Calorie_Consumed
        if gender and age and height and weight and consumed_calorie:
            if gender == "Male":
                bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age) 

                if bmr > consumed_calorie:
                    msg = """
                            You Need to consumed more calorie to gain weight 
                            Now you will lose weight.
                          """
                elif bmr == consumed_calorie:
                    msg = """
                            You are not gain or lose weight.
                          """
                elif bmr < consumed_calorie:
                    msg = """
                            You Need to consumed less calorie to lose weight 
                            Now you will gain weight.
                          """
        
            else:
                bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)

                if bmr > consumed_calorie:
                    msg = """
                            You Need to consumed more calorie to gain weight 
                            Now you will lose weight.
                          """
                elif bmr == consumed_calorie:
                    msg = """
                            You are not gain or lose weight.
                          """
                elif bmr < consumed_calorie:
                    msg = """
                            You Need to consumed less calorie to lose weight 
                            Now you will gain weight.
                          """

            
    else:
        return redirect('userlogin')
        
    context = {
        'bmr' : bmr,
        'msg' :msg
    }
    return render(request, 'homepage.html',context)

@login_required
def userInfo(request):
    userInfo = UserInfo.objects.get(user=request.user)
    context = {
        'userInfo' : userInfo
    }
    return render(request,'userInfo.html',context)

@login_required
def calorieInfo(request):
    calorieInfo = CalorieInfo.objects.get(user=request.user)
    context = {
        'calorieInfo' : calorieInfo
    }
    return render(request,'calorieInfo.html',context)

@login_required
def editUserInfo(request):
    userInfo = request.user.userinfo
    if request.method == "POST":
            form = UserInfoForm(request.POST,instance=userInfo)
            if form.is_valid():
                form.save()
                return redirect('homepage')
    else:
        form = UserInfoForm(instance=userInfo)
    return render(request,'editUserInfo.html',{'form':form}) 
@login_required
def editCalorieInfo(request):
    #user = request.user
    calorieInfo = request.user.calorieinfo
    if request.method == "POST":
            form = CalorieInfoForm(request.POST,instance=calorieInfo)
            if form.is_valid():
                form.save()
                return redirect('homepage')
    else:
        form = CalorieInfoForm(instance=calorieInfo)
    return render(request,'editCalorieInfo.html',{'form':form}) 

def registration(request):
    if(request.method == "POST"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            
            user.save()
            UserInfo.objects.create(user=user)
            CalorieInfo.objects.create(user=user)
            return redirect('userlogin')
    else:
        form = RegistrationForm()
    return render(request,'registrationform.html',{'form':form})


def userlogin(request):
    if request.method=="POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('homepage')
    else:
        form = LoginForm()

    return render(request,'loginForm.html',{'form':form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('registration')