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

    url(r'^shop/(?P<category_slug>[-\w]+)/$', views.product_list_by_category, name='product_list_by_category'),
    url(r'^shop/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^add_category/', views.create_category, name='add_category'),
    url(r'^add_product/', views.create_product, name='add_product'),
    url(r'^add/', views.create_category, name='category_add'),
    url(r'^add_product/', views.create_product, name='product_add'),
    ]
