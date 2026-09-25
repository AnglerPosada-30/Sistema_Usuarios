# WorkBase - Sistema Integrado de Gestión de Personal

**Autor:** Angler Jose Posada Miranda  
**Institución:** INACAP - Ingeniería Informática  
**Módulo:** Desarrollo Backend con Django (Evaluación 2)  

---

## Descripción del Proyecto
WorkBase es una plataforma web desarrollada en Python con Django, diseñada para gestionar la información del personal, estructura organizacional e historial laboral de una empresa. El sistema implementa una arquitectura segura basada en roles (RBAC), separando estrictamente las vistas y privilegios entre administradores (personal de RRHH) y usuarios estándar (trabajadores).

Este proyecto va más allá de un CRUD tradicional, incorporando una interfaz de usuario (UI) premium de nivel empresarial, microinteracciones asíncronas y protección de integridad referencial a nivel de base de datos.

---

## Funcionalidades Principales

###  Seguridad y Autenticación (RBAC)
* **Login y Registro Premium:** Interfaz de pantalla dividida (Split-Screen) con diseño corporativo y validación de credenciales.
* **Control de Acceso:** Uso de `LoginRequiredMixin` y `UserPassesTestMixin` para proteger las rutas. Un usuario sin privilegios que intente acceder a módulos administrativos será interceptado y redirigido.
* **Vistas Dinámicas:** El menú de navegación y la barra lateral (Sidebar) se renderizan condicionalmente dependiendo de si el usuario logueado es `superuser` o un usuario estándar.

### Módulo Administrativo (Exclusivo Superusuarios)
* **Gestión Organizacional:** CRUD completo de `Departamentos` y `Cargos`.
* **Ficha de Trabajadores:** Registro y administración de empleados vinculando llaves foráneas con validación de estado (Activo/Inactivo) y RUT único.
* **Trazabilidad (Historial Laboral):** Registro de la evolución del trabajador dentro de la empresa, controlando fechas de inicio y fin de cada cargo.
* **Django Admin Personalizado:** El panel nativo de Django fue configurado con `list_display`, `search_fields` y `list_filter` para ofrecer búsquedas avanzadas e indexación rápida.

###  Portal del Empleado (Usuarios Estándar)
* **Mi Perfil:** Vista de detalle (`DetailView`) inteligente que detecta la sesión actual y renderiza la ficha técnica de solo lectura del empleado asociado.
* **Historial Personalizado:** Sobrescritura del método `get_queryset()` para garantizar que un usuario común solo pueda visualizar su propio historial laboral en el sistema, aislando los datos del resto de la organización.

---

##  Tecnologías y Stack

**Backend:**
* Python 3
* Django (Vistas Basadas en Clases: `ListView`, `CreateView`, `UpdateView`, `DeleteView`, `DetailView`)
* Django ORM (Manejo de relaciones relacionales, `CASCADE` y protección contra registros huérfanos con `PROTECT`).

**Frontend:**
* HTML5 / CSS3 / Django Templates
* Bootstrap 5 (Grillas, Cards, Modales, Utilidades de espaciado)
* Bootstrap Icons

**Interactividad y UX:**
* **DataTables.js:** Paginación, ordenamiento y búsqueda dinámica en tablas sin recargar la página.
* **SweetAlert2:** Reemplazo de las alertas nativas de javascript por modales elegantes para la confirmación de eliminación de registros, evitando borrados accidentales.
* **Toasts Notifications:** Sistema de alertas flotantes temporales (Top-End) capturando los `messages` de Django (Success/Error).

---

##  Estructura de Base de Datos
El ORM de Django gestiona las siguientes entidades principales:
1. `User`: Maneja todos los usuarios registrados en el sistema.
2. `Rol`: Maneja que tipo de usuario intenta ingresar al sistema, si es administrador, o si es un usuario común
1. `Departamento`: Maneja los centros de costo/áreas (Ej. Informática, Finanzas).
2. `Cargo`: Define los puestos de trabajo.
3. `Trabajador`: Entidad central. Posee relación `OneToOne` con el modelo `User` de Django, y `ForeignKey` protegidas hacia `Departamento` y `Cargo`.
4. `HistorialLaboral`: Tabla transaccional que registra la línea de tiempo de un trabajador en distintos cargos y áreas.

---

##  Instalación y Configuración Local

Si deseas correr este proyecto en tu entorno local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/AnglerPosada-30/Sistema_Usuarios.git

   cd sistema_usuarios

2. **Crear y activar un entorno virtual**
    ```bash
    python -m venv venv
    ```

    - En Windows:
    ```bash
    venv\Scripts\Activate
    ```

    - En Linux/Mac:
    ```bash
    source venv\bin\activate
    ```

3. Instalar dependencias:

    ```bash
    pip install django
    ```

4. Aplicar migraciones a la base de datos:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Crear un superusuario (Administrador del Sistema):

    ```bash
    python manage.py createsuperuser
    ```

6. Ejecutar el servidor local:

    ```bash
    python manage.py runserver
    ```

---

**Este Sistema fué desarrollado con dedicación para demostrar competencias avanzadas en arquitectura de software y deseño de interfaces.**

