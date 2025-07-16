from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm

# Create your views here.

def data(request):
    return render(request,"dataapp/mainpage.html")

def mainpage(request):
    return render(request,"dataapp/mainpage.html")

def about(request):
    return render(request,"dataapp/aboutus.html")

def register(request):
    return render(request,"dataapp/register.html")

def login(request):
    return render(request,"dataapp/login.html")

def services(request):
    return render(request,"dataapp/services.html")


def appointment(request):
    return render(request,"dataapp/appointment.html")

def consultation(request):
    return render(request,"dataapp/onlineconsult.html")


from django.shortcuts import render
from .models import Patient
# Create your views here.

def person_list(request):
    people = Patient.objects.all()
    return render(request,"dataapp/person_list.html",{'people':people})

def add_person(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PatientForm()
    return render(request,'dataapp/add_person.html',{'form':form})

