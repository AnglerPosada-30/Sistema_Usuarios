from django.apps import AppConfig

class AuditoriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auditoria'

    # Agregamos este método para que Django conecte las señales al arrancar el servidor
    def ready(self):
        import auditoria.signals