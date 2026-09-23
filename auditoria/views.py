from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import AuditoriaActividad

class AuditoriaListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = AuditoriaActividad
    template_name = 'auditoria/lista_auditoria.html'
    context_object_name = 'registros'
    # Ordenamos de más nuevo a más viejo
    ordering = ['-fecha_hora'] 

    # Esta es la prueba de seguridad: si retorna False, bloquea el acceso
    def test_func(self):
        return self.request.user.is_superuser