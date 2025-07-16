from django.urls import path
from . import views

urlpatterns = [
    path("data/",views.data,name="data"),path("persons/",views.person_list,name="person_list")
    path('add/' , views.add_person , name = 'add_persons'),
]
