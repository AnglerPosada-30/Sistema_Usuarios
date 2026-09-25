# Este archivo contiene los formularios ModelForm utilizados para gestionar los datos
# de la aplicación organizacion. Cada formulario se vincula a un modelo específico y
# define los campos, etiquetas y widgets que se mostrarán en la interfaz.

from django import forms
from .models import Departamento, Trabajador, Cargo, HistorialLaboral

# Creamos el formulario basado en el modelo departamento.

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento

        # Se indica que campos serán mostrados en el formulario.
        fields = ['nombre', 'codigo_area']
        # Se usa labels para personalizar la interfáz, haciéndola más amigable.
        labels = {
            'nombre': 'Nombre del Departamento',
            'codigo_area': 'Código de Área (Centro de Costo)'
        }


# Creamos el formulario que permitirá crear o editar trabajadores.
class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador

        # Incluimos 'usuario' para vincular al trabajador como un usuario del sistema.
        fields = ['usuario', 'rut', 'nombres', 'apellidos', 'fecha_nacimiento', 'correo', 'telefono', 'departamento', 'cargo', 'fecha_ingreso', 'estado']

        # Personalizamos como se renderizan algunos campos
        widgets = {

            #Agregamos estilo al 'ususario', 'fecha_ingreso', 'fecha_nacimiento'
            'usuario': forms.Select(attrs={'class': 'form-select'}),
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            
        }


# Ahora generamos el formulario que getiona los cargos dentro de la organización
       
class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre', 'descripcion'] 
        labels = {
            'nombre': 'Nombre del Cargo',
            'descripcion': 'Descripción del Cargo'
        }


# En última estancia de este archivo, creamos el formulario para el historial laboral
# Permite seleccionar: el trabajador, el departamento, el cargo y las fechas de inicio y termino
class HistorialLaboralForm(forms.ModelForm):
    class Meta:
        model = HistorialLaboral
        fields = ['trabajador', 'departamento', 'cargo', 'fecha_inicio', 'fecha_fin']
        widgets = {

            # Usamos 'DateInput' para que las fechas se ingresen mediante un calendario.
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }