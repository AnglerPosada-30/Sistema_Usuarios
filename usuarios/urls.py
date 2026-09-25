# Este archivo urls.py contiene la configuración de rutas de la aplicación de usuarios.
# Su función es vincular cada URL con la vista correspondiente, permitiendo gestionar acciones
# como registro, inicio de sesión, edición de perfil y cierre de sesión.

# Importamos path.
from django import views
from django.urls import path

# Importamos la vista de inicio de sesión que proporciona Django. Esta vista se encargará de mostrar el formulario de inicio de sesión y de procesar los datos ingresados por el usuario.
from django.contrib.auth.views import (LoginView, LogoutView)

# Importamos la vista de registro de usuarios que hemos creado en el archivo views.py
from .views import bienvenida, editar_perfil, eliminar_cuenta, registro_usuario

# Definimos las rutas de la aplicación usuarios. En este caso, definimos una ruta para la vista de registro de usuarios.
urlpatterns = [
    # Definimos la ruta para la vista de registro de usuarios. Cuando el usuario acc
    path('registro/', registro_usuario, name='registro'),

    # Definimos la ruta para la vista de inicio de sesión. Cuando el usuario acceda a la ruta 'login/', se mostrará el formulario de inicio de sesión.
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),

    # Definimos la ruta para la vista de bienvenida. Cuando el usuario acceda a la ruta 'bienvenida/', se mostrará la página de bienvenida.
    path('bienvenida/', bienvenida, name='bienvenida'),

    # Definimos la ruta para la vista de edición de perfil. Cuando el usuario acceda a la ruta 'editar_perfil/', se mostrará el formulario de edición de perfil.
    path('editar_perfil/', editar_perfil, name='editar_perfil'),

    #Definimos la ruta para la vista de eliminación de cuenta. Cuando el usuario acceda a la ruta 'eliminar_cuenta/', se mostrará la página de eliminación de cuenta.
    path('eliminar_cuenta/', eliminar_cuenta, name='eliminar_cuenta'),

    #Ahora definimos la ruta para la vista de cierre de sesión. Cuando el usuario acceda a la ruta 'logout/', se cerrará la sesión del usuario y se redirigirá a la página de inicio de sesión.

    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
]