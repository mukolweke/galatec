from django.shortcuts import render, get_object_or_404
from .models import Category, Products
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product/list.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Products, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'product/detail.html', {'product': product, 'cart_product_form': cart_product_form})

# class IndexView(generic.ListView):
#     template_name = 'shop_index.html'
#     context_object_name = 'all_category'
#
#     def get_queryset(self):
#         return Category.objects.all()
#
#
# class DetailView(generic.DetailView):
#     model = Category
#     template_name = 'detail.html'
#
#
# class CategoryCreate(CreateView):
#     title = "Add Category"
#     model = Category
#     fields = ['category_name',  'category_desc', 'category_logo']
#
#
# class CategoryUpdate(UpdateView):
#     title = "Edit Category"
#     model = Category
#     fields = ['category_name',  'category_desc', 'category_logo']
#
#
# class CategoryDelete(DeleteView):
#     model = Category
#     success_url = reverse_lazy('gala:shop')

