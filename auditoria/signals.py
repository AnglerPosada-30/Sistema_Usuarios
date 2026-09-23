from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from organizacion.models import Cargo, Trabajador, Departamento, HistorialLaboral
from .models import AuditoriaActividad

@receiver(post_save, sender=Trabajador)
@receiver(post_save, sender=Departamento)
@receiver(post_save, sender=Cargo)
@receiver(post_save, sender=HistorialLaboral)
def auditar_guardado(sender, instance, created, **kwargs):
    accion = 'CREATE' if created else 'UPDATE'
    nombre_tabla = sender.__name__
    
    usuario_autor = getattr(instance, '_usuario', None)
    
    # NUEVA REGLA: Si hay usuario pero es anónimo, lo convertimos en None
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
    
    # NUEVA REGLA: Validación de seguridad
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