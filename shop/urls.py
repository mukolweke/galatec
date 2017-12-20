from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    # home page
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^category/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),

]
