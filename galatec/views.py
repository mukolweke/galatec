from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', context=None)


def login(request):
    return render(request, 'login.html', context=None)


def registration(request):
    return render(request, 'registration.html', context=None)


def chart(request):
    count = 0;
    return render(request, 'chart.html', context=None)


def test_page(request):
    return render(request, 'test_page.html', context=None)