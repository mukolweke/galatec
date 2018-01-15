from django.conf.urls import url
from . import views

app_name = 'gala'

urlpatterns = [
    # home page
    url(r'^$', views.admin_index, name='index'),

    url(r'^shop/', views.shop_view, name='shop'),
    url(r'^videos/', views.videos, name='videos'),
    url(r'^chart/', views.chart, name='chart'),
    url(r'^orders/', views.orders, name='orders'),

    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^add_category/', views.create_category, name='add_category'),
    url(r'^add_product/', views.create_product, name='add_product'),

    url(r'^add_product/', views.ProductCreate.as_view(), name='product-add'),
    # add category /gala/shop/add_category
    url(r'^add_category/$', views.CategoryCreate.as_view(), name='category-add'),
    # # update category /gala/shop/edit_category/2
    url(r'^edit_category/(?P<pk>[0-9]+)$', views.CategoryUpdate.as_view(), name='category-edit'),
    # # delete category /gala/shop/edit_category/2
    url(r'^(?P<pk>[0-9]+)/delete/$', views.CategoryDelete.as_view(), name='delete-category'),
    ]
