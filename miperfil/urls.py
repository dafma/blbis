__author__ = 'mrk2'
from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^mis_favorito/$', views.mis_favoritos, name='mis_favoritos'),
    url(r'^mis_productos/$', views.mis_productos, name='mis_productos'),
    url(r'^productos_rentados/$', views.productos_rentados, name='productos_rentados'),

    url(r'^publicar/$', views.publica, name='publicar'),

    url(r'^add_remove_bookmark/(\d+)/(\d+)/$', views.add_remove_bookmark),

]
