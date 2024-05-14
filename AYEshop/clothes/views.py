from django.shortcuts import render
from .models import Articles


def clothes_home(request):
    clothes = Articles.objects.all()
    return render(request, 'clothes/clothes_home.html', {"clothes": clothes})


def clothes_man(request):
    clothes = Articles.objects.all()
    return render(request, 'clothes/clothes_man.html', {"clothes": clothes})


def clothes_woman(request):
    clothes = Articles.objects.all()
    return render(request, 'clothes/clothes_woman.html', {"clothes": clothes})


def shoes_man(request):
    clothes = Articles.objects.all()
    return render(request, 'clothes/clothes_home.html', {"clothes": clothes})


def shoes_woman(request):
    clothes = Articles.objects.all()
    return render(request, 'clothes/clothes_home.html', {"clothes": clothes})


def shoes_home(request):
    clothes = Articles.objects.all()
    return render(request, 'clothes/clothes_home.html', {"clothes": clothes})


def accessories(request):
    clothes = Articles.objects.all()
    return render(request, 'clothes/clothes_home.html', {"clothes": clothes})


def new(request):
    return render(request, 'clothes/clothes_home.html')