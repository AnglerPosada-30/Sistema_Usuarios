from django import forms
from .models import Departamento, Trabajador, Cargo, HistorialLaboral

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'codigo_area']
        labels = {
            'nombre': 'Nombre del Departamento',
            'codigo_area': 'Código de Área (Centro de Costo)'
        }

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['rut', 'nombres', 'apellidos', 'fecha_nacimiento', 'telefono', 'departamento', 'cargo']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre', 'descripcion'] 
        labels = {
            'nombre': 'Nombre del Cargo',
            'descripcion': 'Descripción del Cargo'
        }

class HistorialLaboralForm(forms.ModelForm):
    class Meta:
        model = HistorialLaboral
        fields = ['trabajador', 'departamento', 'cargo', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }