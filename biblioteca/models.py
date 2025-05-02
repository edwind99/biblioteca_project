from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# CREAMOS LOS MODELOS AUTOR, LIBRO Y RESEÑA
# DEFINIMOS LAS VALIDACIONES (CAMPO VACIO Y MINIMO DE CARACTERES)


def validar_vacio(valor):
    if not valor.strip():
        raise ValidationError('Este campo no puede estar vacío.')


class Autor(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_vacio])
    fecha_nacimiento = models.DateField(null=False, blank=False)
    nacionalidad = models.CharField(max_length=100, validators=[validar_vacio])

    def __str__(self):
        return self.nombre


def validar_resumen(valor):
    if len(valor) < 20:
        raise ValidationError('El resumen debe tener mínimo 20 caracteres.')


class Libro(models.Model):
    titulo = models.CharField(max_length=100, validators=[validar_vacio])
    autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    resumen = models.TextField(validators=[validar_resumen])

    def __str__(self):
        return self.titulo


# VALIDAMOS LA CALIFICACION DE 0 A 5 CON LOS VALIDADORES QUE TIENE DJANGO

class Resena(models.Model):
    libro = models.ForeignKey(
        Libro, on_delete=models.CASCADE, related_name='resenas')
    texto = models.TextField()
    calificacion = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion}/5.0"
