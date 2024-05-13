from django.urls import path
from . import views

urlpatterns = [
    path('', views.clothes_home, name='clothes_home')
]
