from django.shortcuts import render, get_object_or_404
from .forms import ReservacionForm
from productos.models import Product

def reservacion(request, pk):
    form = ReservacionForm()
    producto = get_object_or_404(Product,
                                 id=pk,
                                 active=True)

    template = "reserva.html"
    return render(request, template, {"form": form, "prod": producto, }
                  )

def despuesfecha(request):
    usuario = request.user
    if request.method == 'POST':
        reseracion_form = ReservacionForm(request.POST)
    return render(request, 'pago_pos_reservacion.html', {})

