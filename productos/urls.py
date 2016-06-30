__author__ = 'mrk2'
from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^prod/(?P<pk>\d+)/$', views.producto_detalle, name='producto_detalle'),



    # todos los productos categorias
    url(r'^productos/$', views.producto, name='producto'),
    url(r'^servicios/$', views.servicios, name='servicios'),
    url(r'^inmuebles/$', views.inmuebles, name='inmuebles'),
    url(r'^transporte/$', views.transporte, name='transporte'),


]