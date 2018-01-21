from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic

from cart.forms import CartAddProductForm
from shop.models import Category, Products

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def admin_index(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html', {'title': 'Login Here'})
    else:
        return render(request, 'dash.html', context=None)


def shop_view(request, category_slug=None):
    if not request.user.is_authenticated():
        return render(request, 'login.html', {'title': 'Login Here'})
    else:
        category = None
        categories = Category.objects.all()
        products = Products.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'shop.html', {'category': category, 'categories': categories, 'products': products})


def create_category(request, category_slug=None):
    if not request.user.is_authenticated():
        return render(request, 'login.html', {'title': 'Login Here'})
    else:
        category = None
        categories = Category.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
        if request.method == 'POST':
            category = Category()
            category.name = request.POST['category_name']
            category.slug = request.POST['category_slug']
            category.save()
            return render(request, 'create_product.html', {'category': category, 'categories': categories})
        return render(request, 'create_category.html', {'category': category, 'categories': categories})


def create_product(request, category_slug=None):
    if not request.user.is_authenticated():
        return render(request, 'login.html', {'title': 'Login Here'})
    else:
        category = None
        categories = Category.objects.all()
        products = Products.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
        if request.method == 'POST':
            cat = get_object_or_404(Category, name=request.POST['category_name'])
            product = Products()
            product.category = cat
            product.name = request.POST['product_name']
            product.slug = request.POST['product_slug']
            product.image = request.FILES['product_img']
            product.description = request.POST['product_desc']
            product.stock = request.POST['product_stock']
            product.price = request.POST['product_prize']
            product.save()
            return render(request, 'shop.html', {'category': category, 'categories': categories})
        return render(request, 'create_product.html', {'category': category, 'categories': categories})


def product_list_by_category(request, category_slug=None):
    if not request.user.is_authenticated():
        return render(request, 'login.html', {'title': 'Login Here'})
    else:
        category = None
        categories = Category.objects.all()
        products = Products.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'shop.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug, category_slug=None):
    if not request.user.is_authenticated():
        return render(request, 'login.html', {'title': 'Login Here'})
    else:
        category = None
        categories = Category.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)

        product = get_object_or_404(Products, id=id, slug=slug, available=True)
        cart_product_form = CartAddProductForm()
        context = {'category': category,
                   'categories': categories,
                   'product': product,
                   'cart_product_form': cart_product_form}
        return render(request,
                      'details.html', context)


def videos(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html', {'title': 'Login Here'})
    else:
        return render(request, 'videos.html', context=None)


def chart(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html', {'title': 'Login Here'})
    else:
        return render(request, 'chart.html', context=None)


def orders(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html', {'title': 'Login Here'})
    else:
        return render(request, 'chart.html', context=None)
