from django.db import models
# Importo AbstractUser porque es la mejor forma de personalizar el modelo de usuario en Django 
# sin tener que reinventar la rueda (ya incluye hashing de contraseñas, validaciones, etc.).
from django.contrib.auth.models import AbstractUser

# Defino una tabla para manejar los roles de mi sistema (ej: Administrador, RRHH, Cajero).
class Rol(models.Model):
    # El nombre del rol debe ser único para no tener confusiones en la asignación de permisos.
    nombre = models.CharField(max_length=50, unique=True)
    
    # La descripción es opcional, solo para documentar qué hace exactamente cada rol.
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        ordering = ['nombre']  # Ordeno alfabéticamente por nombre

# Creo mi propio modelo de Usuario heredando de AbstractUser.
# Esto me permite mantener los campos nativos de Django (username, password, email) 
# y al mismo tiempo agregarle mis propias características.
class Usuario(AbstractUser):
    
    # Creo una relación de "Muchos a Muchos" con la tabla Rol. 
    # Un usuario puede tener varios roles y un rol puede tener muchos usuarios.
    # Con el related_name='usuarios', puedo hacer búsquedas inversas: rol_admin.usuarios.all()
    roles = models.ManyToManyField(Rol, related_name='usuarios', blank=True)
    
    # --- RESOLUCIÓN DE CONFLICTOS INTERNOS DE DJANGO ---
    # Como estoy heredando de AbstractUser, Django intenta crear las relaciones 'groups' 
    # y 'user_permissions' que ya existen en el modelo de usuario nativo. Esto genera un choque.
    # Para evitar que el sistema falle, sobrescribo estos campos y les asigno un 
    # 'related_name' diferente y personalizado ('usuario_set_custom' y 'usuario_permissions_custom').
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set_custom',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions_custom',
        blank=True
    )

    def __str__(self):
        # Muestro el username del usuario en los paneles administrativos por defecto.
        return self.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['username']  # Ordeno alfabéticamente por username

# Defino esta tabla para mantener un registro (auditoría) de cada vez que alguien entra al sistema.
class InicioSesion(models.Model):
    
    # Lo vinculo con mi modelo de Usuario. Aquí uso on_delete=models.CASCADE, 
    # porque si decido eliminar permanentemente a un usuario del sistema, 
    # no me interesa conservar la basura de sus historiales de inicio de sesión.
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='sesiones')
    
    # Uso auto_now_add=True para que Django guarde automáticamente la fecha y hora 
    # exacta del momento en que ocurre el inicio de sesión, sin que yo deba programarlo en la vista.
    fecha_hora = models.DateTimeField(auto_now_add=True)
    
    # GenericIPAddressField es perfecto aquí porque valida automáticamente que el formato 
    # de la IP ingresada sea correcto (IPv4 o IPv6).
    ip_origen = models.GenericIPAddressField(null=True, blank=True)
    
    # Guardo información sobre el navegador o dispositivo (User-Agent) que usó la persona.
    dispositivo = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        # Concateno el usuario y la fecha para identificar rápidamente de qué sesión se trata.
        return f"{self.usuario.username} - {self.fecha_hora}"

    class Meta:
        verbose_name = "Inicio de Sesión"
        verbose_name_plural = "Inicios de Sesión"
        ordering = ['-fecha_hora']  # Ordeno de más reciente a más antiguo  