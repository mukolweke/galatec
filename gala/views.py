from django.shortcuts import render
from shop.models import Category, Products
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.contrib.auth import authenticate, login


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


# Create your views here.
def index(request):
    if not request.user.is_authenticated():
        return render(request, '')
    else:
        return render(request, 'dash.html', context=None)


class ShopView(generic.ListView):

    template_name = 'shop.html'
    context_object_name = 'all_category'

    def get_queryset(self):
        return Category.objects.all()


class DetailView(generic.DetailView):
    model = Category
    template_name = 'details.html'


class ProductCreate(CreateView):
    model = Products
    fields = ['category', 'product_name',  'product_description', 'product_count', 'product_price']


class ProductUpdate(UpdateView):
    model = Products
    fields = ['category', 'product_name',  'product_description', 'product_count', 'product_price']


class ProductDelete(DeleteView):
    model = Products
    success_url = reverse_lazy('gala:detail')


def videos(request):
    return render(request, 'videos.html', context=None)


def chart(request):
    return render(request, 'chart.html', context=None)

