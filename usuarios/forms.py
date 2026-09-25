# Se procede a la importación de la librería de formularios de Django
from django import forms

# Hacemos uso del formulario que incorpora Django para la creación de usuarios
from django.contrib.auth.forms import UserCreationForm

# Se importa el modelo de usuario que incorpora Django
#from django.contrib.auth.models import User

# Se importa el modelo de usuario que hemos creado en la aplicación autenticacion
from django.contrib.auth import get_user_model
User = get_user_model() # Esto trae automáticamente tu modelo 'autenticacion.Usuario'

#Se procede a la creación del formulario de registro de ususarios.

#Heredamos de UserCreationForm para poder hacer uso de los campos que ya tiene incorporado Django para la creación de usuarios.

class RegistroUsuarioForm(UserCreationForm):

    # Se procede a la creación de los campos que se van a utilizar en el formulario de registro de usuarios.
    # Se hace uso de los campos que ya tiene incorporado Django para la creación de usuarios.
    # Se hace uso del campo de correo electrónico que ya tiene incorporado Django para la creación de usuarios.
    email = forms.EmailField(required=True, label='Correo electrónico', help_text='Requerido. Ingrese un correo electrónico válido.')

    class Meta:

        #Se indica que este formulario va a estar asociado al modelo de usuario que incorpora Django.
        model = User

        #Se definen los campos que se van a utilizar en el formulario de registro de usuarios.
        fields = ['username',
                  'first_name',
                  'last_name', 
                  'email', 
                  'password1', 
                  'password2'
                  ]

    def save(self, commit=True):
        user = super(RegistroUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Creamos el formulario para editar el perfil del usuario. Este formulario permitirá al usuario editar su información personal, como su nombre, apellido y correo electrónico.
# Se permite solo modificar esos tres campos.
class EditarPerfilForm(forms.ModelForm):

    class Meta:

        #Trabajamos con User
        model = User

        #Solo se permitirá modificar los siguientes campos del modelo de usuario.
        fields = ['first_name', 
                  'last_name',
                  'email',
                  ]