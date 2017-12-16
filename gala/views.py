from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'gala/dash.html', context=None)


def shop(request):
    return render(request, 'gala/dash.html', context=None)


def videos(request):
    return render(request, 'gala/dash.html', context=None)


def chart(request):
    return render(request, 'gala/dash.html', context=None)
