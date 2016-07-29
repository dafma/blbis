from django.db import models
from django.contrib.auth.models import User
from productos.models import Product
# Create your models here.

class Reservacion(models.Model):
    cliente = models.ForeignKey(User)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    producto = models.ForeignKey(Product)
    renta_pendiente = models.BooleanField(default=False)
    tyc = models.BooleanField('Terminos y condiciones',default=False)
    costo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = "Reservaciones"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return self.cliente.username

    # def get_total_cost(self):
    #     total_cost = sum()
    #     return self.producto.price