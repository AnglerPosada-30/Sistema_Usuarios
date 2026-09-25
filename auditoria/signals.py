# Importamos post_save, post_delete para capturar las señales que disparan despues de un CREATE, UPDATE, DELETE.
from django.db.models.signals import post_save, post_delete

# Importo el decorador receiver que conecta funciones a señales.
from django.dispatch import receiver

#Se importan los modelos que se desean auditar.
from organizacion.models import Cargo, Trabajador, Departamento, HistorialLaboral
#También se importa el modelo donde se guardan los registros
from .models import AuditoriaActividad


@receiver(post_save, sender=Trabajador)
@receiver(post_save, sender=Departamento)
@receiver(post_save, sender=Cargo)
@receiver(post_save, sender=HistorialLaboral)
def auditar_guardado(sender, instance, created, **kwargs):
    accion = 'CREATE' if created else 'UPDATE'
    nombre_tabla = sender.__name__
    
    usuario_autor = getattr(instance, '_usuario', None)
    
    
    if usuario_autor and not usuario_autor.is_authenticated:
        usuario_autor = None
        
    detalle_json = {
        "id_afectado": instance.id,
        "registro": str(instance)
    }

    AuditoriaActividad.objects.create(
        usuario=usuario_autor,
        accion=accion,
        tabla_afectada=nombre_tabla,
        detalle=detalle_json
    )

@receiver(post_delete, sender=Trabajador)
@receiver(post_delete, sender=Departamento)
@receiver(post_delete, sender=Cargo)
@receiver(post_delete, sender=HistorialLaboral)
def auditar_eliminacion(sender, instance, **kwargs):
    nombre_tabla = sender.__name__
    usuario_autor = getattr(instance, '_usuario', None)
    
    
    if usuario_autor and not usuario_autor.is_authenticated:
        usuario_autor = None
        
    detalle_json = {
        "id_eliminado": instance.id,
        "registro": str(instance)
    }

    AuditoriaActividad.objects.create(
        usuario=usuario_autor,
        accion='DELETE',
        tabla_afectada=nombre_tabla,
        detalle=detalle_json
    )