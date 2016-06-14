__author__ = 'mrk2'
from django import forms


from .models import Reservacion

class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ('fecha_inicio', 'fecha_termino', 'producto', )
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_termino': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

        }


class DateRentForm(forms.Form):
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', })
    ),
    fecha_termino = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', })
    ),
