from rest_framework import serializers
from .models import Autor, Libro, Resena

"""
CREAMOS LOS SERIALIZADORES PARA AUTOR, LIBRO Y RESEÑA
PARA ESTO SE UTILIZA DJANGO REST FRAMEWORK CON EL
OBJETIVO DE PODER CREAR UNA API Y PODER UTILIZAR LOS
MÉTODOS GET,POST,DELETE, ETC.
"""


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    recent_reviews = serializers.SerializerMethodField()
    author_name = serializers.ReadOnlyField(source='autor.nombre')

    def get_recent_reviews(self, obj):
        resenas = obj.resenas.order_by('-fecha')[:5]
        return ResenaSerializer(resenas, many=True).data

    class Meta:
        model = Libro
        fields = '__all__'


class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'
