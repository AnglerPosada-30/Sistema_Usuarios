from django.db import models
# Al igual que en auditoría, importo 'settings' para enlazar de forma segura 
# y dinámica nuestro modelo de usuario personalizado.
from django.conf import settings

# Defino el modelo para las áreas o departamentos de la empresa.
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    
    # Agrego unique=True porque no pueden existir dos departamentos con el mismo 
    # código interno o centro de costo. Esto previene duplicados en la base de datos.
    codigo_area = models.CharField(max_length=20, unique=True)

    # Devuelvo el nombre del departamento para que en los selectores del panel 
    # de administración se lea claramente en lugar de un ID numérico.
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['nombre']  # Ordeno alfabéticamente por nombre

# Defino la tabla para los puestos de trabajo que existen en la organización.
class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    
    # La descripción de las funciones la dejo opcional usando blank=True (para los formularios) 
    # y null=True (para la base de datos), por si se crea un cargo rápido sin mucho detalle.
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ['nombre']  # Ordeno alfabéticamente por nombre

# Este es el modelo central del módulo de RRHH, donde guardo la ficha de cada empleado.
class Trabajador(models.Model):
    # Configuro el RUT como único (unique=True) porque es el identificador nacional 
    # fundamental en Chile y me sirve para evitar registrar a la misma persona dos veces.
    rut = models.CharField(max_length=12, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    
    # El teléfono no siempre es obligatorio, así que permito que quede en blanco.
    telefono = models.CharField(max_length=15, blank=True, null=True)
    
    # --- Relaciones ---
    
    # Vinculo al trabajador con su cuenta de acceso al sistema. 
    # Uso OneToOneField porque un empleado solo puede tener un usuario, y un usuario 
    # solo le pertenece a un empleado.
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        # Si por algún motivo se borra la cuenta de usuario, no quiero perder los datos 
        # laborales del trabajador. Por eso uso SET_NULL en lugar de CASCADE.
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        # related_name me permite buscar los datos laborales de un usuario escribiendo: usuario.trabajador
        related_name='trabajador'
    )
    
    # Asigno el departamento. Aquí lo más crítico es el on_delete=models.PROTECT. 
    # Lo configuré así para que el sistema lance un error si alguien intenta borrar un 
    # departamento que todavía tiene trabajadores asignados, evitando inconsistencias graves.
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, related_name='trabajadores')
    
    # Aplico la misma lógica de protección (PROTECT) para el cargo.
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, related_name='trabajadores')

    def __str__(self):
        # Muestro el nombre completo y el RUT en paréntesis para identificarlo rápidamente.
        return f"{self.nombres} {self.apellidos} ({self.rut})"

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"
        ordering = ['apellidos', 'nombres']  # Ordeno alfabéticamente por apellidos y luego nombres


# Creo esta tabla para mantener la trazabilidad de la vida laboral del empleado. 
# Si solo guardara el cargo actual en la tabla 'Trabajador', perdería la historia de sus ascensos.
class HistorialLaboral(models.Model):
    
    # Si por algún motivo se elimina por completo al trabajador de la base de datos, 
    # su historial ya no tiene sentido que exista. Por eso aquí sí utilizo CASCADE.
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='historial')
    
    # Al igual que antes, protejo los departamentos y cargos para que no se puedan borrar 
    # si están siendo referenciados en algún registro histórico.
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    
    fecha_inicio = models.DateField()
    
    # Este campo es clave: si el trabajador sigue ocupando este puesto actualmente, 
    # la fecha de fin queda en blanco (null=True, blank=True). Cuando lo cambien de área, 
    # se llena esta fecha y se crea un nuevo registro con fecha_fin en nulo.
    fecha_fin = models.DateField(null=True, blank=True) 

    def __str__(self):
        return f"{self.trabajador.rut} - {self.cargo.nombre}"

    class Meta:
        verbose_name = "Historial Laboral"
        verbose_name_plural = "Historiales Laborales"
        ordering = ['-fecha_inicio']  # Ordeno de más reciente a más antiguo