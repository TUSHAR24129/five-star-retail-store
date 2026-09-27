from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    path('admin/',    admin.site.urls),
    path('',          views.home_view,  name='home'),
    path('about/',    views.about_view, name='about'),
    path('products/', include('products.urls')),
    path('cart/',     include('cart.urls')),
    path('accounts/', include('accounts.urls')),
    path('orders/',   include('orders.urls')),
    path('contact/',  include('contact.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]