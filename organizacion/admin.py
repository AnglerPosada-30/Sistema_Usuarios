#Importamos el módulo admin de Django y los modelos que queremos registrar en el panel de administración.
from django.contrib import admin
from .models import Departamento, Cargo, Trabajador, HistorialLaboral

#Creamos un modelo de administración para el modelo Trabajador, el cual nos permitirá personalizar la forma en que se muestran los datos de la organización en el panel de administración.
admin.site.register(Departamento)
admin.site.register(Cargo)
admin.site.register(Trabajador)
admin.site.register(HistorialLaboral)