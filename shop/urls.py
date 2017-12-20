from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    # home page
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^category/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    # add category /gala/shop/add_category
    url(r'^add_category/$', views.CategoryCreate.as_view(), name='category-add'),
    # update category /gala/shop/edit_category/2
    url(r'^edit_category/(?P<pk>[0-9]+)$', views.CategoryUpdate.as_view(), name='category-update'),
    # delete category /gala/shop/edit_category/2
    url(r'^(?P<pk>[0-9]+)/delete/$', views.CategoryDelete.as_view(), name='delete-category'),
]
