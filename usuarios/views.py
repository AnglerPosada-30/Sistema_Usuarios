# Este archivo views.py contiene la lógica de las vistas de la aplicación usuarios.
# Cada vista se encarga de recibir la petición del navegador, procesar la información
# enviada y devolver la página HTML adecuada, además de manejar operaciones como
# registro, edición de perfil y eliminación de cuenta.


#render me permite cargar un archivo  html
#redirect me permite redireccionar a una url
from django.shortcuts import render, redirect

#Ahora importamos el formulario de registro de usuarios que hemos creado en el archivo forms.py
from .forms import (
   RegistroUsuarioForm, 
   EditarPerfilForm,
)

#Importamos el decorador login_required, el cual nos permitirá proteger las vistas que requieran que el usuario esté autenticado para poder acceder a ellas.
from django.contrib.auth.decorators import login_required



#Creamos la vista responsable del registro de usuarios, la cual se encargará de mostrar el formulario de registro de usuarios y de procesar los datos ingresados por el usuario.
def registro_usuario(request):

    #Se Comprueba si el navegador está enviando información mediante el método POST
    if request.method == 'POST':

        # Se crea una instancia del formulario de registro de usuarios con los datos enviados por el navegador
        form = RegistroUsuarioForm(request.POST)

        #Se Comprueba si el formulario es válido, es decir, si los datos ingresados por el usuario cumplen con las validaciones definidas en el formulario.
        if form.is_valid():

            # Se guarda el usuario en la base de datos. Django se encargará de guardar el usuario en la tabla de usuarios que incorpora Django.
            form.save()


            return redirect('login')  # Redirige a la página de inicio de sesión después del registro exitoso

        
    else:

        #Si solamente se está accediendo a la vista, es decir, si el navegador no está enviando información mediante el método POST, se crea una instancia vacía del formulario de registro de usuarios.
        form = RegistroUsuarioForm()

    #Se muestra el archivo HTML del formulario de registro de usuarios, pasando como contexto el formulario de registro de usuarios.    
    return render(request, 'usuarios/registro.html', {'form': form})


# login_required significa que solamente
# usuarios autenticados pueden acceder.
@login_required
def bienvenida(request):
 return render(
 request,
 'usuarios/bienvenida.html'
 )


@login_required
def editar_perfil(request):

    #Se Comprueba si el navegador está enviando información mediante el método POST
    if request.method == 'POST':

        #request.POST contiene los datos nuevos.

        #instance=request.user indica que se va a modificar el usuario que está actualmente autenticado.
        form = EditarPerfilForm(request.POST, instance=request.user)

        #Si el formulario es válido.
        if form.is_valid():

            #Guardamos los cambios.
            form.save()

            #Regresamos a la página de bienvenida.
            return redirect('bienvenida')
    else:

        #Cuando solamente abrimos la página, 
        #Mostramos los datos actuales del usuario en el formulario.
        form = EditarPerfilForm(instance=request.user)

    return render(request, 'usuarios/editar_perfil.html', {'form': form})


@login_required
def eliminar_cuenta(request):

    #Por serguridad, solamente eliminamos la cuenta si el navegador está enviando información mediante el método POST.
    if request.method == 'POST':

        usuario = request.user  # Obtenemos el usuario autenticado

        # Eliminamos el usuario autenticado
        usuario.delete()

        return redirect('login')  # Redirige a la página de inicio de sesión después de eliminar la cuenta

    #Si todavía no confirmó, mostramos la página de confirmación de eliminación de cuenta.
    return render(request, 'usuarios/eliminar_cuenta.html')