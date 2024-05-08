from django.shortcuts import render
from .models import Articles


def clothes_home(request):
    clothes = Articles.objects.all()
    return render(request, 'clothes/clothes_home.html', {"clothes": clothes})
