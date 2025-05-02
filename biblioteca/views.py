from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Avg
from .serializer import AutorSerializer, LibroSerializer, ResenaSerializer
from .models import Autor, Libro, Resena


# Create your views here.

"""
AQUÍ CREAMOS NUESTRAS VISTAS DE LOS MODELOS
TAMBIÉN AGREGAMOS DOS MÉTODOS Y CREAMOS UNA RUTA
PARA CALCULAR EL PROMEDIO DE UN LIBRO.

SE INSTALÓ EL MÓDULO DJANGO FILTERS PARA FILTRAR
ESPECÍFICAMENTE POR EL ID DEL AUTOR AL IGUAL
QUE ORDENAR.
"""


class AutorView(viewsets.ModelViewSet):
    serializer_class = AutorSerializer
    queryset = Autor.objects.all()


class LibroView(viewsets.ModelViewSet):
    serializer_class = LibroSerializer
    queryset = Libro.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['autor']  # Para filtrar por ID del autor
    ordering_fields = ['fecha_publicacion', 'titulo']

    def get_queryset(self):
        return Libro.objects.all().order_by('titulo')

    @action(detail=True, methods=['get'])
    def promedio_calificacion(self, request, pk=None):
        libro = self.get_object()
        promedio = libro.resenas.aggregate(Avg('calificacion'))[
            'calificacion__promedio']
        return Response({'promedio_calificacion': promedio})


class ResenaView(viewsets.ModelViewSet):
    serializer_class = ResenaSerializer
    queryset = Resena.objects.all()

    def perform_create(self, serializer):
        if serializer.validated_data['calificacion'] < 2.9:
            print("Reseña negativa")
        serializer.save()
