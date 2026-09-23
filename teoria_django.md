# Teoría y Dudas resultas en la Creación del proyecto.

* **¿Para que me sirve 'manage.py?'**

-En primer lugar, este me permite cargar la configuración correcta del proyecto. Es decir, al ejecutar cualquier comando, **manage.py** establece automáticamente la variable **DJANGO_SETTINGS_MODULE** para que django sepa qué archivo **settings.py** usar. Esto evita que se tenga que hacer la configuración manual cada vez.

-📦 2. Agrega tu proyecto al sys.path
Esto permite que Python encuentre tus módulos y apps internas sin rutas raras.
Es una diferencia clave respecto a usar django-admin directamente. 

🛠️ 3. Ejecuta los comandos esenciales del día a día
Con manage.py puedes:

Levantar el servidor  
python manage.py runserver

Crear migraciones  
python manage.py makemigrations

Aplicar migraciones  
python manage.py migrate

Crear apps  
python manage.py startapp nombre_app

Crear superusuarios  
python manage.py createsuperuser

Abrir la shell interactiva  
python manage.py shell

Ejecutar tests  
python manage.py test  

⚙️ 4. Permite crear comandos personalizados
Puedes definir tus propios comandos dentro de una app (carpeta management/commands) y ejecutarlos con:

Código
python manage.py mi_comando
Esto es útil para tareas automáticas, scripts de mantenimiento, carga de datos, etc. 

🎯 En resumen
manage.py es el archivo que:

Te permite interactuar con tu proyecto Django de forma simple, segura y con la configuración correcta.

Sin él, tendrías que configurar rutas y variables de entorno manualmente cada vez que quisieras ejecutar un comando.


La **razón principal** para preferir el sistema de usuarios que Django ya trae es que **es mucho más seguro, completo y probado** que cualquier tabla casera que puedas crear desde cero.  
Además, evita errores graves que suelen aparecer cuando uno intenta “reinventar” la autenticación.

A partir de las fuentes consultadas, Django ofrece un sistema **robusto, seguro y ya integrado con el admin**, con manejo correcto de contraseñas, permisos y sesiones   [leapcell.io](https://leapcell.io/blog/django-authentication-a-dual-path-journey). También permite extender el modelo sin romper nada usando `AbstractUser`   [djangoproject.in](https://djangoproject.in/blog/django-custom-user-model/).

---

## 🎯 Resumen rápido
**Usar el sistema de usuarios de Django es mejor porque:**

- Es **seguro** (hashing, salting, protección contra ataques).
- Está **probado por miles de proyectos**.
- Se integra automáticamente con el **admin**, permisos y sesiones.
- Evita errores difíciles de corregir en el futuro.
- Permite **extender** el modelo sin perder compatibilidad.

---

¿Por qué crees que es mejor utilizar el sistema de usuarios que Django ya incorpora en
lugar de crear desde cero una tabla con usuario y contraseña?

## 🧠 Razones detalladas

### 🔐 1. Seguridad profesional desde el primer minuto  
Django implementa:
- Hashing seguro de contraseñas  
- Salting  
- Manejo de sesiones  
- Autenticación con backends  
- Protección contra ataques comunes  

Todo esto ya viene probado y mantenido por la comunidad. Crear tu propia tabla con contraseña implica **replicar manualmente** estas medidas, y es muy fácil hacerlo mal.

Las fuentes destacan que el sistema es **robusto y seguro**, con años de mejoras y revisiones de seguridad   [leapcell.io](https://leapcell.io/blog/django-authentication-a-dual-path-journey).

---

### ⚙️ 2. Integración automática con el admin  
El modelo de usuario de Django funciona de inmediato con:
- Django Admin  
- Permisos  
- Grupos  
- Formularios de autenticación  

Si creas tu propia tabla, **pierdes toda esta integración** y tendrías que reescribirla tú mismo.

---

### 🧩 3. Evitas problemas futuros con migraciones  
Cambiar el modelo de usuario después de haber creado migraciones es **muy difícil** y puede romper tu proyecto.  
Las fuentes indican que esta decisión debe tomarse al inicio y que cambiarla después es “doloroso”   [djangoproject.in](https://djangoproject.in/blog/django-custom-user-model/).

Si usas el sistema de Django desde el principio, evitas ese riesgo.

---

### 🛠️ 4. Puedes extender el modelo sin reinventarlo  
Si necesitas campos extra (rut, teléfono, avatar, rol, etc.), puedes usar `AbstractUser`, que ya incluye todo lo necesario y te permite agregar campos sin reescribir la autenticación completa   [djangoproject.in](https://djangoproject.in/blog/django-custom-user-model/).

---

### 🔗 5. Compatibilidad con todo el ecosistema Django  
Django y sus librerías esperan que uses el sistema de usuarios oficial.  
Si creas tu propia tabla, tendrás que adaptar:
- Formularios  
- Middlewares  
- Permisos  
- Autenticación  
- Integraciones externas  

Es mucho trabajo y muy propenso a errores.

---

## 🧾 Tabla comparativa

| Opción | Ventajas | Desventajas |
|-------|----------|-------------|
| **Usuario de Django (recomendado)** | Seguro, probado, integrado con admin, extensible, compatible con todo | Ninguna relevante |
| **Tabla propia con usuario/contraseña** | Control total (pero innecesario) | Riesgos de seguridad, no integra con admin, rompe permisos, requiere reescribir autenticación |

---

## 🧠 Conclusión
Usar el sistema de usuarios de Django **no es solo más fácil**, es **más seguro, más estable y más profesional**.  
Crear tu propia tabla solo tiene sentido si necesitas un sistema de autenticación completamente distinto (por ejemplo, login solo con teléfono o sin contraseña), algo que las fuentes también mencionan como casos excepcionales   [djangoproject.in](https://djangoproject.in/blog/django-custom-user-model/).

---

