from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy


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