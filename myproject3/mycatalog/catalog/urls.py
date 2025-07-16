from django.urls import path
from . import views

urlpatterns = [
    path('ops/', views.operations),  # Route to test product operations
]
