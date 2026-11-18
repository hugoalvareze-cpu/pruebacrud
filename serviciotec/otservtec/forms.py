from django import forms
from django_select2.forms import Select2Widget
from .models import OrdenTrabajo, CambioBateria, Cliente, Equipo, Tecnico, Zona, Estado, Bateria
        
class OrdenTrabajoForm(forms.ModelForm):
    class Meta:
        model = OrdenTrabajo
        fields = '__all__'
        widgets = {
            # Asignar la clase 'select2' a los campos desplegables
            'id_cliente': forms.Select(attrs={'class': 'form-select select2'}),
            'id_equipo': forms.Select(attrs={'class': 'form-select select2'}),
            'id_zona': forms.Select(attrs={'class': 'form-select select2'}),
            'id_tecnico': forms.Select(attrs={'class': 'form-select select2'}),
            'id_estado': forms.Select(attrs={'class': 'form-select select2'}),
            
            # Formato de fechas y cuadros de texto
            'fecha_ingreso': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_termino': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_retiro': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'materiales': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'info_retiro': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_cliente', 'apellido_cli', 'email_cliente', 'telefono']
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente'}),
            'apellido_cli': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido del cliente'}),
            'email_cliente': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56 9 ...'}),
        }

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['id_anam', 'numero_serie', 'marca', 'modelo', 'descripcion']
        widgets = {
            'id_anam': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID ANAM'}),
            'numero_serie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de serie'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del equipo'}),
        }

class ZonaForm(forms.ModelForm):
    class Meta:
        model = Zona
        fields = ['zona']
        widgets = {
            'zona': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: Zona Norte, Centro, Sur...'
            }),
        }

class CambioBateriaForm(forms.ModelForm):
    class Meta:
        model = CambioBateria
        fields = [
            'num_bateria',
            'id_cliente',
            'id_zona',
            'id_tecnico',
            'info_retiro',
            'fecha_solicitud_bateria',
            'fecha_retiro_bateria',
        ]
        widgets = {
            'fecha_solicitud_bateria': forms.DateInput(attrs={'type': 'date'}),
            'fecha_retiro_bateria': forms.DateInput(attrs={'type': 'date'}),
            'observacion': forms.Textarea(attrs={'rows': 3}),
        }
        
class BateriaForm(forms.ModelForm):
    class Meta:
        model = Bateria
        fields = ['num_bateria', 'marca', 'modelo', 'descripcion']
        widgets = {
            'num_bateria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de batería'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción de la batería'}),
        }