# # Declaramos la configuración de la aplicación autenticacion. Esta clase permite a Django
# identificar la app, inicializar sus componentes y gestionar su integración dentro del proyecto.

from django.apps import AppConfig


class AutenticacionConfig(AppConfig):
    name = 'autenticacion'
