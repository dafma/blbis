from django.shortcuts import render, get_object_or_404
from .forms import ReservacionForm, DateRentaForm
from productos.models import Product

def reservacion(request, pk):
    formr = DateRentaForm()
    # if request.method == 'POST':
    #     if form.is_valid():
    #         inicio = form.cleaned_data['fecha_inicio']
    #         fin = form.cleaned_data['fecha_termino']
    #         diasTotales = abs((inicio-fin).days)
    #         return render(request, 'pago_pos_reservacion.html')
    producto = get_object_or_404(Product,
                                 id=pk,
                                 active=True)
    template = "reserva.html"
    context = {
        "formr": formr,
        "prod": producto,
    }
    return render(request, template, context)

def despuesfecha(request):
    usuario = request.user
    if request.method == 'POST':
        reseracion_form = ReservacionForm(request.POST)
    return render(request, 'pago_pos_reservacion.html', {})

