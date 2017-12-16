from django.conf.urls import url
from . import views

app_name = 'videos'

urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),
]
