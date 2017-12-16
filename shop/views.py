from django.shortcuts import render
from django.http import Http404
from .models import Category


# Create your views here.
def index(request):
    all_category = Category.objects.all()
    return render(request, 'shop/index.html', {'all_category': all_category})


def detail(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404("Category Unknown")
    return render(request, 'shop/detail.html', {'category': category})