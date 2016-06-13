from django.shortcuts import render, get_object_or_404
from .forms import ReservacionForm, DateRentForm
from productos.models import Product

def reservacion(request, pk):
    form = DateRentForm()
    if form.is_valid():
        inicio = form.cleaned_data['fecha_inicio']
        fin = form.cleaned_data['fecha_termino']
        diasTotales = abs((inicio-fin).days)

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

