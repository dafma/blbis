__author__ = 'mrk2'
from django import forms



from .models import Reservacion

class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ('fecha_inicio', 'fecha_termino','tyc', )
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'datepicker1'}),
            'fecha_termino': forms.DateInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'datepicker2'}),
            'tyc': forms.CheckboxInput(attrs={'required':'true',})

        }


class DateRentaForm(forms.Form):
    inicio = forms.DateField(widget=forms.DateInput()),
    # termino = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', })),


