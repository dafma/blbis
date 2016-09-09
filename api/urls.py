from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'productos', views.PProductViewSet)
# router.register(r'servicios', views.SProductPViewSet)
# router.register(r'transporte', views.TProductPViewSet)
# router.register(r'inmobiliario', views.IProductPViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]