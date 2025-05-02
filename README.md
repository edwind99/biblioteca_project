# 📚 Biblioteca Project

Proyecto web desarrollado con **Django** para gestionar autores, libros y reseñas.

## Funcionalidades (NUEVAS)

- Registro de **Autores**, **Libros** y **Reseñas** desde el panel de administración.
- Validaciones personalizadas.
- Relaciones entre entidades/modelos.

- ¡New! Se modificó el modelo Reseña
- ¡New! Se implementó REST FRAMEWORK para el uso de serializer, views, rutas y filtros.
  🔹 Serializadores
  Uso de ModelSerializer para los tres modelos.
  En LibroSerializer:
  author_name: muestra el nombre del autor.
  recent_reviews: muestra las 5 reseñas más recientes del libro.

  🔹Se crearon ModelViewSet para cada modelo.

  🔹Rutas generadas automáticamente con DefaultRouter bajo el prefijo /api/.

  🔹Posibilidad de:
  Filtrar libros por autor: /api/libros/?autor=1
  Ordenar libros por título o fecha: /api/libros/?ordering=-fecha_publicacion

  🔹Paginación activada con 5 resultados por página (por defecto)
  🔹Ruta personalizada con @action para obtener el promedio de calificaciones de un libro con la ruta: /api/libros/<id>/promedio_calificacion/

## COMENTARIOS EXPLICATIVOS ACERCA DE:

1.  SerializerMethodField: En este proyecto se utilizó SerializerMethodField dentro de LibroSerializer para incluir un campo llamado recent_reviews. Este campo muestra las 5 reseñas más recientes de un libro. Esta técnica permite mejorar la API sin alterar la estructura del modelo.

2.  Filtros y Ordenamiento (django-filter): Se integró el paquete django-filter para permitir al cliente filtrar libros por autor y ordenarlos por título o fecha de publicación. Esta funcionalidad hace que la API sea más flexible y útil para cuando se requiera una búsqueda avanzada.

3.  Paginación: Para evitar sobrecargar la respuesta de la API con gran cantidad de datos, se implementó la paginación. Esto permite dividir los resultados en páginas manejables utilizando parámetros. Esto mejora la eficiencia del servidor, reduce el uso de ancho de banda y optimiza la experiencia del usuario.

4.  Ruta personalizada con @action: Se definió una ruta personalizada utilizando @action dentro del ViewSet de libros para calcular el promedio de calificación de un libro. Esta funcionalidad encapsula una operación lógica específica que no encaja con los métodos de un CRUD estándar, pero que es útil en el modelo.

## Requisitos

- Python 3.8 o superior
- Django 4.x

## 📥 Instalación

1. **Clona el repositorio en alguna carpeta o en tu escritorio.**:

```bash
git clone https://github.com/edwind99/biblioteca_project.git
cd biblioteca_project
```

2. **Crea un entorno virtual (venv)**:

```bash
python -m venv venv
# Activar en Windows
venv\Scripts\activate
# Activar en Mac/Linux
source venv/bin/activate
```

3. **Instala las dependencias**:

```bash
pip install -r requirements.txt
```

4. **Aplica las migraciones**:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crea un superusuario para acceder al panel de administración.**:

```bash
python manage.py createsuperuser
```

6. **Ejecuta el servidor**:

```bash
python manage.py runserver
```

7. **Ejecuta el script para poblar los datos de la base de datos de ejemplo (OPCIONAL)**:

```bash
exec(open('poblar_datos.py').read())
```

## Screenshots

## Panel de admin

![Panel de admin](screenshots/panel_admin.png)
![Autores](screenshots/autores.png)
![Libros](screenshots/libros.png)
![Reseñas](screenshots/resenas.png)

## Script

![Script](screenshots/script.png)

## Script ejecutado

![Script ejecutado](screenshots/script_ejecutado.png)

## ✍️ Créditos

Proyecto realizado para la materia de Programación Web.
Integrantes:

1. Edwin Andres Duarte Rodriguez - 1152055
2. Diego Alexander Bermudez Florez - 1152067
   Profesor: Daniel Andres Esteban Carrillo.
