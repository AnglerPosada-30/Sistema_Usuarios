from django.db import models
# Importo 'settings' de django.conf para poder referenciar dinámicamente al modelo 
# de usuario, lo cual es una mejor práctica que importarlo directamente.
from django.conf import settings

# Defino el modelo que será la tabla en la base de datos encargada de registrar 
# todo lo que pasa en el sistema, funcionando como una bitácora de seguridad intocable.
class AuditoriaActividad(models.Model):
    
    # Construyo una llave foránea para vincular cada evento con la persona exacta que ejecutó la acción.
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, # Uso la referencia al usuario configurado en mi settings.py
        
        # Regla vital para auditoría: si el día de mañana eliminamos a un trabajador del sistema, 
        # no quiero que sus registros de actividad se borren en cascada. El registro se mantendrá 
        # intacto, simplemente el autor pasará a ser "nulo".
        on_delete=models.SET_NULL, 
        null=True, # Necesario para que la base de datos acepte que el usuario quede en nulo.
        
        # Agrego este atajo para que, si tengo un objeto usuario, pueda consultar 
        # rápidamente todo su historial de acciones escribiendo: usuario.logs.all()
        related_name='logs' 
    )
    
    # Campo de texto corto donde registro y estandarizo qué tipo de operación ocurrió.
    accion = models.CharField(max_length=50) # Ej: 'CREATE', 'UPDATE', 'DELETE'
    
    # Campo de texto que utilizo para identificar en qué entidad del sistema impactó el cambio.
    tabla_afectada = models.CharField(max_length=100) # Ej: 'Trabajador', 'Departamento'
    
    # Le asigno auto_now_add=True para delegarle el trabajo a Django. Así captura 
    # automáticamente la marca de tiempo exacta del servidor en el instante en que se crea 
    # el registro, evitando que yo tenga que insertarla manualmente.
    fecha_hora = models.DateTimeField(auto_now_add=True)
    
    # Decidí usar un JSONField porque la estructura de lo que cambia varía dependiendo de la acción.
    # Aquí puedo inyectar un diccionario JSON mostrando exactamente el antes y el después 
    # (ej: {"cargo_anterior": "Analista", "cargo_nuevo": "Gerente"}). Esto me da la flexibilidad 
    # de auditar cualquier tabla sin tener que crear columnas adicionales.
    detalle = models.JSONField(null=True, blank=True) 

    # Sobrescribo este método para mejorar la legibilidad en el panel de administración o consola.
    # En lugar de que Django me devuelva un texto ilegible como "AuditoriaActividad object (1)", 
    # me devolverá una cadena clara y concatenada.
    def __str__(self):
        return f"{self.accion} en {self.tabla_afectada} por {self.usuario}"

    class Meta:
        verbose_name = "Actividad de Auditoría"
        verbose_name_plural = "Actividades de Auditoría"
        ordering = ['-fecha_hora'] # El signo menos indica orden descendente