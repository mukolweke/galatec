from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from shop.models import Category, Products
from cart.forms import CartAddProductForm

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def index(request):
    # if not request.user.is_authenticated():
    #     return render(request, '')
    # else:
    return render(request, 'dash.html', context=None)


def shop_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop.html', {'category': category, 'categories': categories, 'products': products})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

    product = get_object_or_404(Products, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'details.html', {'category': category, 'categories': categories, 'product': product, 'cart_product_form': cart_product_form})


def create_category(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'create_category.html', {'category': category, 'categories': categories})


def create_product(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'create_product.html', {'category': category, 'categories': categories})


class DetailView(generic.DetailView):
    model = Category
    template_name = 'details.html'


class CategoryCreate(CreateView):
    title = "Add Category"
    model = Category
    fields = ['name',  'slug']


class CategoryUpdate(UpdateView):
    title = "Edit Category"
    model = Category
    fields = ['category_name',  'category_desc', 'category_logo']


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('gala:shop')


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


def orders(request):
    return render(request, 'chart.html', context=None)

