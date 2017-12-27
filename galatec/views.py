from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'galatec/index.html', context=None)


def login(request):
    return render(request, 'galatec/login.html', context=None)


def forget(request):
    return render(request, 'galatec/forget.html', context=None)


def registration(request):
    return render(request, 'galatec/registration.html', context=None)


def chart(request):
    count = 0;
    return render(request, 'galatec/chart.html', context=None)


def test_page(request):
    return render(request, 'galatec/test_page.html', context=None)