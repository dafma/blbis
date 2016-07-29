__author__ = 'mrk2'
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rentas import views


urlpatterns = [
    url(r'^rent/(?P<pk>\d+)/$', views.reservacion, name='reservacion'),
    # url(r'^process/$', views.payment_process, name='process'),
    url(r'^done/$', views.payment_done, name='done'),
    url(r'^canceled/$', views.payment_canceled, name='canceled'),

]
