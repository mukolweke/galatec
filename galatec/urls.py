from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'galatec'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # home page
    url(r'^$', views.index, name='index'),
    url(r'^gala/', include('gala.urls'), name='gala'),
    url(r'^login/', views.login, name='login'),
    url(r'^forgot', views.forget, name='forget'),
    url(r'^register', views.registration, name='register'),
    # shop url page
    url(r'^shop/', include('shop.urls'), name='shop'),
    # videos url page
    url(r'^videos/', include('videos.urls'), name='videos'),
    # chart url page
    url(r'^chart/', views.chart, name='chart'),
]
