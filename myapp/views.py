from django.shortcuts import render, redirect
from django.http import request
from .models import *
from django.contrib.auth import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    return

def homepage(request):
    bmi = Job.objects.all()
    users = CustomUser.objects.all()
    context = {
        "jobs": jobs
    }
    return render(request, 'homepage.html', context)


def registration(request):
    if(request.method == "POST"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
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