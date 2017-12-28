from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views
from accounts.views import (login_view, register_view, forget_view, logout_view)

app_name = 'galatec'

urlpatterns = [
    # django admin-dev page only
    url(r'^admin/', admin.site.urls),
    # admin user section
    url(r'^galaAdmin/', include('gala.urls'), name='gala'),
    # customer user section
    url(r'^$', views.index, name='index'),
    # customer access
    url(r'^shop/', include('shop.urls'), name='shop'),
    url(r'^videos/', include('videos.urls'), name='videos'),
    url(r'^chart/', views.chart, name='chart'),
    # accounts
    url(r'^login/$', login_view, name='login'),
    url(r'^forgot/$', forget_view, name='forget'),
    url(r'^register/$', register_view, name='register'),
    url(r'^logout/$', logout_view, name='logout'),
    # test page
    url(r'^test/$', views.test_page, name='test'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
