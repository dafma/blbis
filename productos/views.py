from django.shortcuts import render, get_object_or_404
from .models import Product
from blog.models import Post

# Create your views here.
def index(request):
    # categoria fiestas
    prodFiestas = Product.objects.filter(categories__title="fiestas")[:8]
    # categoria carros
    prodCarros = Product.objects.filter(categories__title="carros")[:8]
    # categoria inmuebles
    prodInmuebles = Product.objects.filter(categories__title="Inmuebles")
    # ultimos productos solo da 4
    ultimosProductos = Product.objects.all()[:5]
    # productos que quiza te interesen
    prodIntereses = Product.objects.order_by('?')[:8]
    # recomendaciones
    prodRecomendaciones = Product.objects.order_by('?')[:8]

    # nlog ultimas 3
    ultimasTresEntradas = Post.objects.all()[:3]

    context = {
        "inmuebles": prodInmuebles,
        "ultimosProductos": ultimosProductos,
        'prodCarros': prodCarros,
        "prodFiestas": prodFiestas,
        "prodIntereses": prodIntereses,
        "prodRecomendaciones": prodRecomendaciones,
        "ultimas3Entradas": ultimasTresEntradas,
    }
    return render(request, 'index.html',  context)

def producto_detalle(request, pk):
    producto = get_object_or_404(Product,
                                 id=pk,
                                 active=True)
    return render(request, 'detalle_product.html', {'producto': producto, })


def producto(requets):
    prod = Product.objects.filter(categories__title="Inmuebles")
    context = {
        "prod":prod,
    }
    return render(requets, 'categorias_productos/productos.html')

def servicios(requets):
    prod= Product.objects.filter(categories__title="fiestas")
    context = {
        "prod":prod,
    }
    return render(requets, 'categorias_productos/servicios.html', context)

def inmuebles(requets):
    prod = Product.objects.filter(categories__title="Inmuebles")
    context = {
        "prod":prod,
    }
    return render(requets, 'categorias_productos/inmuebles.html', context)

def transporte(requets):
    prod= Product.objects.filter(categories__title="carros")
    context = {
        "prod":prod,
    }
    return render(requets, 'categorias_productos/transporte.html', context)