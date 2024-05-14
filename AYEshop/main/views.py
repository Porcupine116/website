from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/home.html', data)


def about(request):
    return render(request, 'main/about.html')


def purchase(request):
    return render(request, 'main/home.html')


def favorites(request):
    return render(request, 'main/about.html')


def paymant(request):
    return render(request, 'main/about.html')


def search(request):
    return render(request, 'main/about.html')