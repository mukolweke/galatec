from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'user_home.html', context=None)


def about_us(request):
    return render(request, 'about_us.html', context=None)


def terms(request):
    return render(request, 'terms.html', context=None)


def faqs(request):
    return render(request, 'faqs.html', context=None)


def contact_us(request):
    return render(request, 'contact_us.html', context=None)


def login(request):
    return render(request, 'login.html', context=None)


def registration(request):
    return render(request, 'registration.html', context=None)


def chart(request):
    count = 0;
    return render(request, 'chart.html', context=None)


def test_page(request):
    return render(request, 'test_page.html', context=None)