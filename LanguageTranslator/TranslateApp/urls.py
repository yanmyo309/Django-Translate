from django.urls import path
from .views import Login,Translate

urlpatterns = [
    path('',Login,name='login'),
    path('transLanguage/',Translate,name='translate')
]
