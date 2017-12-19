from django.conf.urls import url

from . import views
app_name = 'gala'

urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),
    url(r'^shop/', views.shop, name='shop'),
    url(r'^videos/', views.videos, name='videos'),
    url(r'^chart/', views.chart, name='chart'),


]
