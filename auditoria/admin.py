from django.contrib import admin
from .models import AuditoriaActividad

# Para que se vea como una tabla detallada en el panel
class AuditoriaActividadAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'accion', 'tabla_afectada', 'fecha_hora')
    list_filter = ('accion', 'tabla_afectada')
    readonly_fields = ('fecha_hora',)

admin.site.register(AuditoriaActividad, AuditoriaActividadAdmin)