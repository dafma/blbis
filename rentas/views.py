from django.shortcuts import render, get_object_or_404
from .forms import ReservacionForm, DateRentaForm
from productos.models import Product
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rentas.models import Reservacion

from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

@login_required
def reservacion(request, pk):
    form = ReservacionForm()
    cliente = request.user
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
            reserva = Reservacion(cliente=cliente,producto=producto,
                                                 fecha_inicio=inicio, fecha_termino=fin,
                                                 costo=total)
            ulReserva = Reservacion.objects.filter(cliente=cliente).last()
            reserva.save()
            id_reserva = ulReserva.id
            reserva = get_object_or_404(Reservacion, id=id_reserva)
            host = request.get_host()

            paypal_dict = {
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'amount':'%.2f' % reserva.costo,
                'item_name':'Renta del producto {}'.format(reserva.producto),
                'invoice':str(reserva.id),
                'currency_code':'USD',
                'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
                'return_url':'http://{}{}'.format(host, reverse('rentas:done')),
                'cancel_return': 'http://{}{}'.format(host, reverse('rentas:canceled')),
            }
            form = PayPalPaymentsForm(initial=paypal_dict)
            # # rentadia =
            context = {
                'total':total,
                'producto':producto,
                'inicio':inicio,
                'fin':fin,
                'ulReserva':ulReserva,
                'form':form,
                'diasTotales':diasTotales,
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


# def payment_process(request):
#     paquete_id = request.POST.get('paquete', False)
#     reserva = get_object_or_404(Reservacion, id=1)
#     host = request.get_host()
#
#     paypal_dict = {
#             'business': settings.PAYPAL_RECEIVER_EMAIL,
#             'amount':'%.2f' % reserva.costo,
#             'item_name':'Renta del producto {}'.format(reserva.producto),
#             'invoice':str(reserva.id),
#             'currency_code':'USD',
#             'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
#             'return_url':'http://{}{}'.format(host, reverse('rentas:done')),
#             'cancel_return': 'http://{}{}'.format(host, reverse('rentas:canceled')),
#         }
#     form = PayPalPaymentsForm(initial=paypal_dict)
#     return render(request, 'process.html',{'order':reserva, 'form':form})

@csrf_exempt
def payment_done(request):
    return render(request, 'done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request, 'canceled.html')