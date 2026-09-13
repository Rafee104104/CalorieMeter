from django.shortcuts import render, redirect
from django.http import request
from .models import *
from django.contrib.auth import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
# Create your views here.


def bmr(request):   
    total_calorie = CalorieInfo.objects.filter(
        users=request.user,
        date=timezone.localdate()
    ).aggregate(
        total=Sum('Calorie_Consumed')
    )['total'] or 0
    height = request.user.userinfo.Height
    weight = request.user.userinfo.Weight
    age = request.user.userinfo.Age
    gender = request.user.userinfo.Gender
    bmr = None
    msg = ""
    none_msg = ""
    if gender and age and height and weight and total_calorie is not None:
        if gender.lower() == "male":
            bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age) 

            if bmr > total_calorie:
                msg = """
                        You Need to consumed more calorie to gain weight 
                        Now you will lose weight.
                        """
            elif bmr == total_calorie:
                msg = """
                        You are not gain or lose weight.
                        """
            elif bmr < total_calorie:
                msg = """
                        You Need to consumed less calorie to lose weight 
                        Now you will gain weight.
                        """
    
        else:
            bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)

            if bmr > total_calorie:
                msg = """
                        You Need to consumed more calorie to gain weight 
                        Now you will lose weight.
                        """
            elif bmr == total_calorie:
                msg = """
                        You are not gain or lose weight.
                        """
            elif bmr < total_calorie:
                msg = """
                        You Need to consumed less calorie to lose weight 
                        Now you will gain weight.
                        """
    else:
        none_msg = "Please Input height, weight, age, gender and consumed calories"
    request.user.userinfo.bmr = bmr
    request.user.userinfo.save()
    
        
    context = {
        'bmr' : bmr,
        'msg' :msg,
        'none_msg' : none_msg,
        'total_calorie' : total_calorie
    }
    return render(request, 'bmr.html',context)
@login_required
def homepage(request):
    return render(request,'homepage.html')

@login_required
def userInfo(request):
    userinfo = UserInfo.objects.filter(
        users=request.user
    )
    context = {
        'userInfo' : userinfo
    }
    return render(request,'userInfo.html',context)

@login_required
def calorieInfo(request):
    calorieInfo = CalorieInfo.objects.filter(
        users=request.user
    ).order_by('-date')
    context = {
        'calorieInfo' : calorieInfo
    }
    return render(request,'calorieInfo.html',context)

@login_required
def editUserInfo(request):
    user = CustomUser.objects.get(id=request.user.id)
    userInfo = user.userinfo  
    if request.method == "POST":
            form = UserInfoForm(request.POST,instance=userInfo)
            if form.is_valid():
                form.save()
                return redirect('userInfo')
    else:
        form = UserInfoForm(instance=userInfo)
    return render(request,'editUserInfo.html',{'form':form}) 
@login_required
def editCalorieInfo(request):
    user =CustomUser.objects.get(id=request.user.id)
    calorieInfo = user.calorieinfo
    if request.method == "POST":
            form = CalorieInfoForm(request.POST,instance=calorieInfo)
            if form.is_valid():
                form.save()
                return redirect('homepage')
    else:
        form = CalorieInfoForm()
    return render(request,'editCalorieInfo.html',{'form':form}) 

def registration(request):
    if(request.method == "POST"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            
            user.save()
            userinfo = UserInfo(
                users=user
            )
            userinfo.save()
            calorieinfo = CalorieInfo(
                users=user
            )
            calorieinfo.save()
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