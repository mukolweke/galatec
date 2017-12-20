from django.shortcuts import render
from shop.models import Category
from django.views import generic


# Create your views here.
def index(request):
    return render(request, 'gala/dash.html', context=None)


class ShopView(generic.ListView):
    template_name = 'gala/shop.html'
    context_object_name = 'all_category'

    def get_queryset(self):
        return Category.objects.all()


class DetailView(generic.DetailView):
    model = Category
    template_name = 'gala/details.html'


def videos(request):
    return render(request, 'gala/videos.html', context=None)


def chart(request):
    return render(request, 'gala/chart.html', context=None)
