__author__ = 'mrk2'
from django import forms



from .models import Reservacion

class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ('fecha_inicio', 'fecha_termino', 'producto','tyc', )
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_termino': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            # 'tyc': forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-control'}),

        }


class DateRentaForm(forms.Form):
    inicio = forms.DateField(widget=forms.DateInput()),
    # termino = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', })),


