from django.shortcuts import render
from .serializers import ProductSerializer
# Create your views here.
from productos.models import Product
from rest_framework import viewsets

# productos servicios transporte e inmuebles

class PProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(categories__title="Inmuebles")
    serializer_class = ProductSerializer


class SProductPViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(categories__title="fiestas")
    serializer_class = ProductSerializer


class TProductPViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(categories__title="carros")
    serializer_class = ProductSerializer

class IProductPViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(categories__title="Inmuebles")
    serializer_class = ProductSerializer

