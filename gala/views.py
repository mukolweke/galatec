from django.shortcuts import render
from shop.models import Category


# Create your views here.
def index(request):
    return render(request, 'gala/dash.html', context=None)


def shop(request):
    all_category = Category.objects.all()
    return render(request, 'gala/shop.html', {'all_category': all_category})


def videos(request):
    return render(request, 'gala/videos.html', context=None)


def chart(request):
    return render(request, 'gala/chart.html', context=None)
