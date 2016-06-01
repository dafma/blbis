from django.db import models
from django.contrib.auth.models import User
from productos.models import Product
# Create your models here.

class Misfavoritos(models.Model):
    usuario = models.ForeignKey(User)
    producto = models.ForeignKey(Product)