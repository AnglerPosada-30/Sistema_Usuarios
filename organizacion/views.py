from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Departamento, Trabajador, Cargo, HistorialLaboral
from .forms import DepartamentoForm, TrabajadorForm, CargoForm, HistorialLaboralForm
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.contrib import messages

# --- ESCUDO DE SEGURIDAD ---
class AdminRequeridoMixin(UserPassesTestMixin):
    # Prueba: ¿Es superusuario?
    def test_func(self):
        return self.request.user.is_superuser

    # Si falla la prueba (es usuario normal), lo pateamos a la bienvenida con una alerta roja
    def handle_no_permission(self):
        messages.error(self.request, "Acceso denegado: Área exclusiva de administración.")
        return redirect('bienvenida')


# --- VISTAS DE DEPARTAMENTOS ---

class DepartamentoListView(AdminRequeridoMixin, ListView):
    model = Departamento
    template_name = 'organizacion/lista_departamentos.html'
    context_object_name = 'departamentos'

class DepartamentoCreateView(AdminRequeridoMixin, CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'organizacion/form_departamento.html'
    success_url = reverse_lazy('lista_departamentos') 

    def form_valid(self, form):
        form.instance._usuario = self.request.user
        return super().form_valid(form)

class DepartamentoUpdateView(AdminRequeridoMixin, UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'organizacion/form_departamento.html'
    success_url = reverse_lazy('lista_departamentos')

    def form_valid(self, form):
        form.instance._usuario = self.request.user
        return super().form_valid(form)

class DepartamentoDeleteView(AdminRequeridoMixin, DeleteView):
    model = Departamento
    template_name = 'organizacion/confirmar_eliminacion.html'
    success_url = reverse_lazy('lista_departamentos')

    def post(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            self.object._usuario = request.user
            self.object.delete()
            messages.success(request, "Departamento eliminado correctamente.")
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Acción denegada: No puedes eliminar este departamento porque tiene trabajadores asignados.")
            return redirect(self.success_url)


# --- VISTAS DE TRABAJADORES ---

class TrabajadorListView(AdminRequeridoMixin, ListView):
    model = Trabajador
    template_name = 'organizacion/lista_trabajadores.html'
    context_object_name = 'trabajadores'

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
        return redirect(self.success_url)


# --- VISTAS DE CARGOS ---

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


# --- VISTAS DE HISTORIAL LABORAL ---

class HistorialListView(AdminRequeridoMixin, ListView):
    model = HistorialLaboral
    template_name = 'organizacion/lista_historial.html'
    context_object_name = 'historiales'

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