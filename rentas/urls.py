__author__ = 'mrk2'
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rentas import views


urlpatterns = [
    url(r'^rent/(?P<pk>\d+)/$', views.reservacion, name='reservacion'),

]
