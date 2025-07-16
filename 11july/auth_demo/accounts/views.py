from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required   #decorators are kind of auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.object.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            User.objects.create_user(username=username , password=password)
            messages.success(request, 'User register successfully')
            return redirect('login')
        
    return render (request , 'accounts/register.html') 

def user_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username , password=password)

        if user:
            login(request, user)
            return redirect('home')
    
        else:
            messages.error(request,'Invalid credentials')

    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/home.html')

def user_logout(request):
    logout(request)
    return redirect('login')