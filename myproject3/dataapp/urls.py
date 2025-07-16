
from django.urls import path
from . import views
urlpatterns = [
    
    path('data/',views.data,name="data"),
    path('main/', views.mainpage, name="mainpage"),
    path('about/', views.about, name="about"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('services/', views.services, name="services"),
    path('appointment/', views.appointment, name="appointment"),
    path('consultation/', views.consultation, name="consultation"),
    path("persons/",views.person_list,name="person_list"),
    path("add/",views.add_person,name="add_person")
]
