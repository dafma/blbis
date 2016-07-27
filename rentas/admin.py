from django.contrib import admin

# Register your models here.
from .models import Reservacion


@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    pass