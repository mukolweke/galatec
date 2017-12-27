from django.conf.urls import url

from . import views
from shop.views import (CategoryCreate, CategoryUpdate, CategoryDelete)
from shop.views import UpdateView,DeleteView

app_name = 'gala'

urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),

    url(r'^shop/', views.ShopView.as_view(), name='shop'),
    url(r'^videos/', views.videos, name='videos'),
    url(r'^chart/', views.chart, name='chart'),
    url(r'^category/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),

    url(r'^add_product/(?P<pk>[0-9]+)$', views.ProductCreate.as_view(), name='product-add'),
    # add category /gala/shop/add_category
    url(r'^add_category/$', CategoryCreate.as_view(), name='category-add'),
    # update category /gala/shop/edit_category/2
    url(r'^edit_category/(?P<pk>[0-9]+)$', CategoryUpdate.as_view(), name='category-edit'),
    # delete category /gala/shop/edit_category/2
    url(r'^(?P<pk>[0-9]+)/delete/$', CategoryDelete.as_view(), name='delete-category'),
    ]
