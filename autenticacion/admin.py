from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Rol, InicioSesion

# Registramos el modelo Usuario heredando de UserAdmin para mantener 
# la funcionalidad de encriptación de contraseñas en el panel.
admin.site.register(Usuario, UserAdmin)

# Registramos también las otras tablas de esta aplicación
admin.site.register(Rol)
admin.site.register(InicioSesion)