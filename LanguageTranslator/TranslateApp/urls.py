from django.urls import path
from .views import Translate

urlpatterns = [
    path('',Translate,name='translate')
]
