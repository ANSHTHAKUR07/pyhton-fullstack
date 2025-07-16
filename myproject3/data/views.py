from django.shortcuts import render
from .models import person
from .models import personForm

# Create your views here.

def data(request):
    if request.method == 'POST':
        form = personForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('person_list') # redirect after Post
        else:
            form =personForm() #initializing an empty form for GET


        return render (request,'data/add_persons.html', { 'form' : form})

