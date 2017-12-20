from django.conf.urls import url

from . import views
from shop.views import UpdateView,DeleteView

app_name = 'gala'

urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),
    url(r'^shop/', views.ShopView.as_view(), name='shop'),
    url(r'^videos/', views.videos, name='videos'),
    url(r'^chart/', views.chart, name='chart'),
    url(r'^category/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    ]
