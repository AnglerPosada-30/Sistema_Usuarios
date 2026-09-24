from django.urls import reverse_lazy
# NUEVO: Importamos DetailView para cumplir con la rúbrica
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Departamento, Trabajador, Cargo, HistorialLaboral
from .forms import DepartamentoForm, TrabajadorForm, CargoForm, HistorialLaboralForm
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.contrib import messages

# --- ESCUDO DE SEGURIDAD (RBAC) ---
class AdminRequeridoMixin(UserPassesTestMixin):
    """
    Este Mixin intercepta la petición antes de cargar la vista.
    Defensa: "Utilizo UserPassesTestMixin para verificar si el usuario tiene el rol de superusuario. 
    Si test_func retorna False, handle_no_permission captura al usuario, lanza una alerta y lo redirige."
    """
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "Acceso denegado: Área exclusiva de administración.")
        return redirect('bienvenida')


# ==========================================
# MÓDULO DE DEPARTAMENTOS
# ==========================================

class DepartamentoListView(AdminRequeridoMixin, ListView):
    """ ListView se encarga automáticamente de hacer un SELECT * FROM Departamento """
    model = Departamento
    template_name = 'organizacion/lista_departamentos.html'
    context_object_name = 'departamentos'

class DepartamentoCreateView(AdminRequeridoMixin, CreateView):
    """ CreateView renderiza un formulario vacío y maneja el INSERT a la base de datos """
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'organizacion/form_departamento.html'
    success_url = reverse_lazy('lista_departamentos') 

    def form_valid(self, form):
        # Defensa: "Sobreescribo form_valid para inyectar silenciosamente qué usuario está haciendo la acción 
        # antes de que Django guarde el registro en la base de datos, útil para la auditoría."
        form.instance._usuario = self.request.user
        return super().form_valid(form)

class DepartamentoUpdateView(AdminRequeridoMixin, UpdateView):
    """ UpdateView busca un registro por su ID (pk) y llena el formulario para hacer un UPDATE """
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'organizacion/form_departamento.html'
    success_url = reverse_lazy('lista_departamentos')

    def form_valid(self, form):
        form.instance._usuario = self.request.user
        return super().form_valid(form)

class DepartamentoDeleteView(AdminRequeridoMixin, DeleteView):
    """ DeleteView maneja la eliminación física (DELETE) de un registro """
    model = Departamento
    template_name = 'organizacion/confirmar_eliminacion.html'
    success_url = reverse_lazy('lista_departamentos')

    def post(self, request, *args, **kwargs):
        # Defensa: "Uso un bloque try-except para capturar ProtectedError. Como mi modelo tiene on_delete=PROTECT, 
        # si intento borrar un departamento con trabajadores, evito que la app colapse y muestro un mensaje amigable."
        try:
            self.object = self.get_object()
            self.object._usuario = request.user
            self.object.delete()
            messages.success(request, "Departamento eliminado correctamente.")
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Acción denegada: No puedes eliminar este departamento porque tiene trabajadores asignados.")
            return redirect(self.success_url)


# ==========================================
# MÓDULO DE TRABAJADORES (EMPLEADOS)
# ==========================================

class TrabajadorListView(AdminRequeridoMixin, ListView):
    model = Trabajador
    template_name = 'organizacion/lista_trabajadores.html'
    context_object_name = 'trabajadores'

# NUEVO: Vista de Detalle solicitada en la pauta (5 puntos)
class TrabajadorDetailView(AdminRequeridoMixin, DetailView):
    """ 
    DetailView hace un SELECT * FROM Trabajador WHERE id = pk. 
    Defensa: "Esta vista cumple el requerimiento de mostrar la ficha completa de un empleado en modo solo lectura."
    """
    model = Trabajador
    template_name = 'organizacion/detalle_trabajador.html'
    context_object_name = 'trabajador'

class TrabajadorCreateView(AdminRequeridoMixin, CreateView):
    model = Trabajador
    form_class = TrabajadorForm 
    template_name = 'organizacion/form_trabajador.html'
    success_url = reverse_lazy('lista_trabajadores')

    def form_valid(self, form):
        form.instance._usuario = self.request.user
        return super().form_valid(form)

class TrabajadorUpdateView(AdminRequeridoMixin, UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'organizacion/form_trabajador.html'
    success_url = reverse_lazy('lista_trabajadores')

    def form_valid(self, form):
        form.instance._usuario = self.request.user
        return super().form_valid(form)

class TrabajadorDeleteView(AdminRequeridoMixin, DeleteView):
    model = Trabajador
    template_name = 'organizacion/confirmar_eliminacion.html'
    success_url = reverse_lazy('lista_trabajadores')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object._usuario = request.user
        self.object.delete()
        messages.success(request, "Trabajador eliminado correctamente.")
        return redirect(self.success_url)


# ==========================================
# MÓDULO DE CARGOS
# ==========================================

class CargoListView(AdminRequeridoMixin, ListView):
    model = Cargo
    template_name = 'organizacion/lista_cargos.html'
    context_object_name = 'cargos'

class CargoCreateView(AdminRequeridoMixin, CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'organizacion/form_cargo.html'
    success_url = reverse_lazy('lista_cargos')

    def form_valid(self, form):
        form.instance._usuario = self.request.user
        return super().form_valid(form)

class CargoUpdateView(AdminRequeridoMixin, UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'organizacion/form_cargo.html'
    success_url = reverse_lazy('lista_cargos')

    def form_valid(self, form):
        form.instance._usuario = self.request.user
        return super().form_valid(form)

class CargoDeleteView(AdminRequeridoMixin, DeleteView):
    model = Cargo
    template_name = 'organizacion/confirmar_eliminacion.html'
    success_url = reverse_lazy('lista_cargos')

    def post(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            self.object._usuario = request.user
            self.object.delete()
            messages.success(request, "Cargo eliminado correctamente.")
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Acción denegada: No puedes eliminar este cargo porque tiene trabajadores asignados.")
            return redirect(self.success_url)


# ==========================================
# MÓDULO DE HISTORIAL LABORAL
# ==========================================

# Asegúrate de importar LoginRequiredMixin arriba si no lo tienes:
# from django.contrib.auth.mixins import LoginRequiredMixin

class HistorialListView(LoginRequiredMixin, ListView):
    model = HistorialLaboral
    template_name = 'organizacion/lista_historial.html'
    context_object_name = 'historiales'

    def get_queryset(self):
        """
        Defensa: 'Sobrescribo get_queryset para aplicar seguridad a nivel de filas. 
        Si el usuario es superadmin, retorna todos los registros de la empresa. 
        Si es un usuario estándar, filtra la base de datos para mostrar únicamente 
        el historial que coincida con su perfil de trabajador.'
        """
        if self.request.user.is_superuser:
            return HistorialLaboral.objects.all()
        else:
            # Filtramos el historial buscando al trabajador vinculado al usuario actual
            return HistorialLaboral.objects.filter(trabajador__usuario=self.request.user)

class HistorialCreateView(AdminRequeridoMixin, CreateView):
    model = HistorialLaboral
    form_class = HistorialLaboralForm
    template_name = 'organizacion/form_historial.html'
    success_url = reverse_lazy('lista_historial')

    def form_valid(self, form):
        form.instance._usuario = self.request.user
        return super().form_valid(form)

class HistorialUpdateView(AdminRequeridoMixin, UpdateView):
    model = HistorialLaboral
    form_class = HistorialLaboralForm
    template_name = 'organizacion/form_historial.html'
    success_url = reverse_lazy('lista_historial')

    def form_valid(self, form):
        form.instance._usuario = self.request.user
        return super().form_valid(form)

class HistorialDeleteView(AdminRequeridoMixin, DeleteView):
    model = HistorialLaboral
    template_name = 'organizacion/confirmar_eliminacion.html'
    success_url = reverse_lazy('lista_historial')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object._usuario = request.user
        self.object.delete()
        messages.success(request, "Registro histórico eliminado correctamente.")
        return redirect(self.success_url)