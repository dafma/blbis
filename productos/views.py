from django.shortcuts import render, get_object_or_404
from .models import Product

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
    context = {
        "inmuebles": prodInmuebles,
        "ultimosProductos": ultimosProductos,
        'prodCarros': prodCarros,
        "prodFiestas": prodFiestas,
    }
    return render(request, 'index.html',  context)

def producto_detalle(request, pk):
    producto = get_object_or_404(Product,
                                 id=pk,
                                 active=True)
    return render(request, 'detalle_product.html', {'producto': producto, })
