from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'galatec'

urlpatterns = [
    # django admin-dev page only
    url(r'^admin/', admin.site.urls),


    # admin user section
    url(r'^gala/', views.login_view, name='gala_login'),
    url(r'^gala_admin/', include('gala.urls'), name='gala_admin'),

    # customer user section
    url(r'^$', views.index, name='index'),
    url(r'^terms/', views.terms, name='terms'),
    url(r'^faqs/', views.faqs, name='faqs'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),

    # customer access
    url(r'^shop/', include('shop.urls'), name='shop'),
    url(r'^videos/', include('videos.urls'), name='videos'),
    url(r'^chart/', views.chart, name='chart'),
    # accounts
    url(r'^login/$', views.login_view, name='login'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^register_user/', views.create_user, name='create_user'),
    url(r'^forgot/$', views.forget_view, name='forget'),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^logout/$', views.logout_user, name='logout'),
    # test page
    url(r'^test/$', views.test_page, name='test'),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
