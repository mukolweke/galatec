from .models import Products,Category
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'all_category'

    def get_queryset(self):
        return Category.objects.all()


class DetailView(generic.DetailView):
    model = Category
    template_name = 'shop/detail.html'


class CategoryCreate(CreateView):
    title = "Add Category"
    model = Category
    fields = ['category_name',  'category_desc', 'category_logo']


class CategoryUpdate(UpdateView):
    title = "Edit Category"
    model = Category
    fields = ['category_name',  'category_desc', 'category_logo']


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('gala:shop')

