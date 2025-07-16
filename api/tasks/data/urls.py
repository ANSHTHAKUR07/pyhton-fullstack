from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import dataViewset

router =DefaultRouter()
router.register(r'data',dataViewset)

urlpatterns = [
    path('' , include(router.urls)),
]
