from django.shortcuts import render
from shop.models import Category,Products
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views import generic
from django.core.urlresolvers import reverse_lazy


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


class ProductCreate(CreateView):
    model = Products
    fields = ['product_name',  'product_description', 'product_count', 'product_price']


class ProductUpdate(UpdateView):
    model = Products
    fields = ['product_name',  'product_description', 'product_count', 'product_price']


class ProductDelete(DeleteView):
    model = Products
    success_url = reverse_lazy('gala:detail')


def videos(request):
    return render(request, 'gala/videos.html', context=None)


def chart(request):
    return render(request, 'gala/chart.html', context=None)
