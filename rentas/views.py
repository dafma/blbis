from django.shortcuts import render, get_object_or_404
from .forms import ReservacionForm, DateRentaForm
from productos.models import Product
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm


@login_required
def reservacion(request, pk):
    form = ReservacionForm()
    if request.method == 'POST':
        formr = ReservacionForm(request.POST)
        producto = request.POST.get('productoid')
        if formr.is_valid():
            inicio = formr.cleaned_data['fecha_inicio']
            fin = formr.cleaned_data['fecha_termino']
            diasTotales = abs((inicio-fin).days)
            producto = Product.objects.get(id =producto)
            precio =  producto.price
            total = diasTotales * precio
            # # rentadia =
            context = {
                'total':total,
                'producto':producto,
                'inicio':inicio,
                'fin':fin,
            }
            return render(request, 'pago_pos_reservacion.html',context)
        else:
            return HttpResponse("nou nou")
    producto = get_object_or_404(Product,
                                 id=pk,
                                 active=True)
    template = "reserva.html"
    context = {
        "formr": form,
        "prod": producto,
    }
    return render(request, template, context)

def despuesfecha(request):
    usuario = request.user
    if request.method == 'POST':
        reseracion_form = ReservacionForm(request.POST)
    return render(request, 'pago_pos_reservacion.html', {})


def payment_process(request):
    pass
