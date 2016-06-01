from django.contrib import admin
from .models import Misfavoritos
# Register your models here.

@admin.register(Misfavoritos)
class MisfavoritosAdmin(admin.ModelAdmin):
    pass
