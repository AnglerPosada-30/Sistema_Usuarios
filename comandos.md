- User.objects.all() --> Obtiene todos los usuarios de la base de datos.

- User.objects.count() --> Cuenta cuantos usuarios hay en la base de datos.

- User.objects.filter(is_active=True) --> Aplicamos un filtro sobre el modelo User para obtener únicamente los usuarios que están marcados como activos en el sistema (is_active=True).

- User.objects.get(username='admin') --> Obtiene el usuario cuyo nombre de usuario es exactamente ‘admin’. Como get() espera un único resultado, si no existe o si hay más de uno, Django lanzará una excepción.

- usuario = User.objects.get(username='admin') -->
Obtengo el usuario cuyo nombre de usuario es ‘admin’ y lo guardo en la variable usuario. Como get() espera un único resultado, si no existe o si hay más de uno, Django lanzará una excepción.
Luego puedo acceder a los atributos del usuario fácilmente de la siguiente manera:

* usuario.username
* usuario.email
* usuario.is_active