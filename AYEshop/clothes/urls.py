from django.urls import path
from . import views

urlpatterns = [
    path('clothes', views.clothes_home, name='clothes'),

    path('clothes/clothes-man', views.clothes_man, name='clothes-man'),
    path('clothes/clothes-woman', views.clothes_woman, name='clothes-woman'),

    path('shoes', views.shoes_home, name='shoes'),

    path('shoes/shoes-man', views.shoes_man, name='shoes-man'),
    path('shoes/shoes-woman', views.shoes_woman, name='shoes-woman'),

    path('accessories', views.accessories, name='accessories'),

    path('NEW', views.new, name='NEW'),
]
