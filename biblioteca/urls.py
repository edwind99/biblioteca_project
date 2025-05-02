from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorView, LibroView, ResenaView


"""
AGREGAMOS LAS RUTAS QUE VAN A TENER NUESTRAS
VISTAS JUNTO CON LA RUTA PADRE API/ Y LUEGO
SE CONFIGURA EN EL ARCHIVO URLS.PY DEL PROYECTO
"""

router = DefaultRouter()
router.register(r'autores', AutorView)
router.register(r'libros', LibroView)
router.register(r'resenas', ResenaView)

urlpatterns = [
    path('api/', include(router.urls)),
]
