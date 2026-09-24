from django.contrib import admin
from .models import Departamento, Cargo, Trabajador, HistorialLaboral

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_area', 'nombre')
    search_fields = ('nombre', 'codigo_area')
    ordering = ('nombre',)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    ordering = ('nombre',)

# AQUÍ ASEGURAMOS LOS PUNTOS DE LA RÚBRICA (list_display, search_fields, list_filter, ordering)
@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    # Columnas que se mostrarán en la tabla del administrador
    list_display = ('rut', 'nombres', 'apellidos', 'cargo', 'departamento', 'estado')
    
    # Agrega una barra de búsqueda por estos campos
    search_fields = ('rut', 'nombres', 'apellidos', 'correo')
    
    # Agrega un panel lateral derecho para filtrar resultados con un solo clic
    list_filter = ('departamento', 'cargo', 'estado')
    
    # Ordenamiento por defecto de la tabla
    ordering = ('apellidos', 'nombres')

@admin.register(HistorialLaboral)
class HistorialLaboralAdmin(admin.ModelAdmin):
    list_display = ('trabajador', 'cargo', 'departamento', 'fecha_inicio', 'fecha_fin')
    list_filter = ('departamento', 'cargo')
    # Buscamos a través de la llave foránea usando doble guion bajo (__)
    search_fields = ('trabajador__rut', 'trabajador__nombres', 'trabajador__apellidos')