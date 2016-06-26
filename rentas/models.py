from django.db import models
from django.contrib.auth.models import User
from productos.models import Product
# Create your models here.

class Reservacion(models.Model):
    cliente = models.ForeignKey(User)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    producto = models.ForeignKey(Product)
    renta_pendiente = models.BooleanField()
    tyc = models.BooleanField('Terminos y condiciones',)

    class Meta:
        verbose_name = "Reservaciones"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return self.cliente.username
