from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import CrearProdForm
from productos.models import Product, ProductImage
from django.contrib.auth.models import User
from .models import Misfavoritos
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def mis_favoritos(request):
    usuario = request.user
    misFavoritos = Misfavoritos.objects.filter(usuario=usuario)
    context = {
        "misFavoritos": misFavoritos,
    }
    return render(request, 'mis_favoritos.html', context)

@login_required
def mis_productos(request):
    usuario = request.user
    misproductos = Product.objects.filter(usuario=usuario)
    context = {
        "misproductos": misproductos,
    }
    return render(request, 'mis_productos.html', context)

@login_required
def productos_rentados(request):
    return render(request, 'productos_rentados.html')

@login_required
def publica(request):
    usuario = request.user
    if request.method == 'POST':
        form = CrearProdForm(request.POST, request.FILES)
        if form.is_valid():
            formv = form.save(commit=False)
            formv.usuario = usuario
            formv.save()
            return redirect("miPerfil:mis_productos")
    form = CrearProdForm()
    template = "productos_publicados/crear.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


def add_remove_bookmark(request, uid, qid):
    try:
        mifavorito = Misfavoritos.objects.get(usuario=uid, producto=qid)
        mifavorito.delete()
    except Misfavoritos.DoesNotExist:
        mifavorito = Misfavoritos.objects.create(
                       usuario=User.objects.get(id=uid),
                       producto=Product.objects.get(id=qid))
        mifavorito.save()
    return redirect("miPerfil:mis_favoritos")


# categocias productos
def inmuebles(request):
    return render(request, "categorias_productos/inmuebles.html")

def productos(request):
    return render(request)

def servicios(request):
    return render(request)

def transporte(request):
    return render(request)

@login_required
class MiproductoUpdate(UpdateView):
    model = Product
    success_url = reverse_lazy('miPerfil:mis_productos')
    fields = ['title', 'description', 'price', 'active', 'num_contacto']

@login_required
class MiproductoDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('miPerfil:mis_productos')

@login_required
class MisFavoritosDelete(DeleteView):
    model = Misfavoritos
    success_url = reverse_lazy('miPerfil:mis_favoritos')

@login_required
class imagenCreate(CreateView):
    model = ProductImage
    template_name = "productos_publicados/add_imagen.html"
    fields = ("product", "image")
    success_url = reverse_lazy('miPerfil:mis_productos')
