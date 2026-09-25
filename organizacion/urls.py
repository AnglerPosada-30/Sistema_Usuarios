from django.urls import path
from .views import (
    DepartamentoListView, DepartamentoCreateView, DepartamentoUpdateView, DepartamentoDeleteView,
    TrabajadorListView, TrabajadorCreateView, TrabajadorUpdateView, TrabajadorDeleteView, TrabajadorDetailView, MiPerfilView,
    CargoListView, CargoCreateView, CargoUpdateView, CargoDeleteView,
    HistorialListView, HistorialCreateView, HistorialUpdateView, HistorialDeleteView
)

urlpatterns = [
    # Departamentos
    path('departamentos/', DepartamentoListView.as_view(), name='lista_departamentos'),
    path('departamentos/nuevo/', DepartamentoCreateView.as_view(), name='crear_departamento'),
    path('departamentos/editar/<int:pk>/', DepartamentoUpdateView.as_view(), name='editar_departamento'),
    path('departamentos/eliminar/<int:pk>/', DepartamentoDeleteView.as_view(), name='eliminar_departamento'),
    
    # Trabajadores
    path('trabajadores/', TrabajadorListView.as_view(), name='lista_trabajadores'),
    path('trabajadores/nuevo/', TrabajadorCreateView.as_view(), name='crear_trabajador'),
    path('trabajadores/detalle/<int:pk>/', TrabajadorDetailView.as_view(), name='detalle_trabajador'),
    path('trabajadores/editar/<int:pk>/', TrabajadorUpdateView.as_view(), name='editar_trabajador'),
    path('trabajadores/eliminar/<int:pk>/', TrabajadorDeleteView.as_view(), name='eliminar_trabajador'),
    path('mi-perfil/', MiPerfilView.as_view(), name='mi_perfil'),

    # Cargos
    path('cargos/', CargoListView.as_view(), name='lista_cargos'),
    path('cargos/nuevo/', CargoCreateView.as_view(), name='crear_cargo'),
    path('cargos/editar/<int:pk>/', CargoUpdateView.as_view(), name='editar_cargo'),
    path('cargos/eliminar/<int:pk>/', CargoDeleteView.as_view(), name='eliminar_cargo'),

    # Historial Laboral
    path('historial/', HistorialListView.as_view(), name='lista_historial'),
    path('historial/nuevo/', HistorialCreateView.as_view(), name='crear_historial'),
    path('historial/editar/<int:pk>/', HistorialUpdateView.as_view(), name='editar_historial'),
    path('historial/eliminar/<int:pk>/', HistorialDeleteView.as_view(), name='eliminar_historial'),
]