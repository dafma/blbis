__author__ = 'mrk2'
from django.conf.urls import url, patterns
from miperfil import views
from .views import (
 MiproductoUpdate,
MiproductoDelete,
MisFavoritosDelete,
imagenCreate,
)


urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^mis_favorito/$', views.mis_favoritos, name='mis_favoritos'),
    url(r'^mis_favoritos/eliminar/(?P<pk>\d+)$', MisFavoritosDelete.as_view(), name='favoritos_eliminar'),
    url(r'^mis_productos/$', views.mis_productos, name='mis_productos'),
    url(r'^mis_productos/editar/(?P<pk>\d+)$', MiproductoUpdate.as_view(), name='producto_edit'),
    url(r'^mis_productos/eliminar/(?P<pk>\d+)$', MiproductoDelete.as_view(), name='producto_eliminar'),
    url(r'^productos_rentados/$', views.productos_rentados, name='productos_rentados'),
    url(r'^add_image/$', imagenCreate.as_view(), name='add_image'),

    url(r'^publicar/$', views.publica, name='publicar'),

    url(r'^add_remove_bookmark/(\d+)/(\d+)/$', views.add_remove_bookmark),


]
