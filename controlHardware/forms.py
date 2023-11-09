from django.forms import ModelForm
from django import forms

from .models import Proveedor
from .models import Fabricante
from .models import Capacidad
from .models import HistorialCompras
from .models import NasModelo
from .models import DiscoModelo


# Crear un widget personalizado para las fechas.
class DateInput(forms.DateInput):
    input_type = 'date'


class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ('nombre', 'activo',)

        widgets = {
           'nombre': forms.widgets.TextInput(attrs={'class': 'form-control'}),
           'activo': forms.widgets.CheckboxInput(attrs={'class': 'form-control'}),
        }


class FabricanteForm(ModelForm):
    class Meta:
        model = Fabricante
        fields = ('nombre', 'activo',)
        widgets = {
            'nombre': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'activo': forms.widgets.CheckboxInput(attrs={'class': 'form-control'}),
        }




class CapacidadForm(ModelForm):
    class Meta:
        model = Capacidad
        fields = ('valor', 'unidadMedida', 'activo',)
        widgets = {
            'valor': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'unidadMedida': forms.widgets.Select(attrs={'class':'form-control'}),
            'activo': forms.widgets.CheckboxInput(attrs={'class': 'form-control'}),
        }


class HistorialComprasForm(ModelForm):
    class Meta:
        model = HistorialCompras
        fields = ('proveedor', 'fechaCompra', 'codigo', 'activo',)
        
        widgets = {
            'proveedor': forms.widgets.Select(attrs={'class':'form-control'}),
            'fechaCompra': DateInput(attrs={'class':'form-control'}),
            'codigo': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'activo': forms.widgets.CheckboxInput(attrs={'class':'form-control'}),
        }



class NasModeloForm(ModelForm):
    class Meta:
        model = NasModelo
        exclude = ('actualizacionUsuario', 'creacionFechaHora', 'actualizacionFechaHora', )

        widgets = {
            'modelo': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'anioLanzamiento': forms.widgets.NumberInput(attrs={'class':'form-control'}),
            'fabricante': forms.widgets.Select(attrs={'class':'form-control'}),
            'garantiaAnios': forms.widgets.Select(attrs={'class':'form-control'}),
            'cantidadBahiasInternas': forms.widgets.NumberInput(attrs={'class':'form-control'}),
            'cantidadUnidadesExpansion': forms.widgets.NumberInput(attrs={'class':'form-control'}),
            'maxCantDiscosUnidadExpansion': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'ramIncluidaGB': forms.widgets.NumberInput(attrs={'class':'form-control'}),
            'ramMax': forms.widgets.NumberInput(attrs={'class':'form-control'}),
            'ramSlots': forms.widgets.NumberInput(attrs={'class':'form-control'}),
            'cantidadNics1Gb': forms.widgets.NumberInput(attrs={'class':'form-control'}),
            'cantidadNics10Gb': forms.widgets.NumberInput(attrs={'class':'form-control'}),
            'cantidadBahiasPci': forms.widgets.NumberInput(attrs={'class':'form-control'}),
            'activo': forms.widgets.CheckboxInput(attrs={'class':'form-control'}),
            'esRackeable': forms.widgets.CheckboxInput(attrs={'class':'form-control'}),
            'tieneFuentePoderRedundante': forms.widgets.CheckboxInput(attrs={'class':'form-control'}),
        }




class DiscoModeloForm(ModelForm):
    class Meta:
        model = DiscoModelo
        exclude = ('actualizacionUsuario', 'creacionFechaHora', 'actualizacionFechaHora', )

        widgets = {
            'modeloCorto': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'modeloLargo': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.widgets.Textarea(attrs={'class':'form-control'}),
            'fabricante': forms.widgets.Select(attrs={'class':'form-control'}),
            'capacidad': forms.widgets.Select(attrs={'class':'form-control'}),
            'esSSD': forms.widgets.CheckboxInput(attrs={'class':'form-control'}),
            'garantiaAnios': forms.widgets.Select(attrs={'class':'form-control'}),
            'rpms': forms.widgets.NumberInput(attrs={'class':'form-control'}),
            'cacheEnMB': forms.widgets.NumberInput(attrs={'class':'form-control'}),
            'activo': forms.widgets.CheckboxInput(attrs={'class':'form-control'}),
        }





# class ProveedorForm(ModelForm):
#     class Meta:
#         model = Proveedor
#         fields = '__all__'



# class ProveedorForm2(forms.Form):
#     nombre = forms.CharField(max_length=30,  widget=forms.widgets.TextInput, label='Desc.:')
#     activo = forms.BooleanField(widget=forms.widgets.CheckboxInput,label="Activo:")
#     fecha = forms.DateField(widget=DateInput, required=False)
