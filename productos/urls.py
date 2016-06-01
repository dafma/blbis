__author__ = 'mrk2'
from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^prod/(?P<pk>\d+)/$', views.producto_detalle, name='producto_detalle'),



    # todos los productos categorias
    url(r'^productos/$', views.producto_detalle, name='productos'),
    url(r'^servicios/$', views.producto_detalle, name='servicios'),
    url(r'^inmuebles/$', views.producto_detalle, name='inmuebles'),
    url(r'^transporte/$', views.producto_detalle, name='transporte'),


]