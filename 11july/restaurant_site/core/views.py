from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def menu(request):
    return render(request, 'menu.html')

def order(request):
    return render(request, 'order.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import MenuItem, Order
from .forms import RegisterForm, OrderForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # hash password
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('menu')
        else:
            error = 'Invalid credentials'
    return render(request, 'login.html', {'error': error})

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'items': items})

@login_required
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('menu')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})

def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['email']  # username or email
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('menu')
        else:
            error = 'Invalid username or password'
    return render(request, 'login.html', {'error': error})
