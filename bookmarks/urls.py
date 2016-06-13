from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^$', 'productos.views.index', name='index'),
    url(r'^mi_perfil/', include('miperfil.urls', namespace="miPerfil")),
    url(r'^productos/', include('productos.urls', namespace="productos")),
    url(r'^rentar/', include('rentas.urls', namespace="rentas")),
    # python-social-auth
    url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
