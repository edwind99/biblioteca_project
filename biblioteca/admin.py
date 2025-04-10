from django.contrib import admin
from .models import Autor, Libro, Resena

# Configuración para mostrar más detalles en el admin
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_nacimiento', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'resumen')
    search_fields = ('titulo', 'autor__nombre')
    list_filter = ('fecha_publicacion',)

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('libro', 'texto', 'calificacion', 'fecha')
    search_fields = ('libro__titulo',)
    list_filter = ('calificacion', 'fecha')
