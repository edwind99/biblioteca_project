from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
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
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    resumen = models.TextField(validators=[validar_resumen])

    def __str__(self):
        return self.titulo
    
def validar_calificacion(valor):
    if valor < 1 or valor > 10:
        raise ValidationError('La calificación debe estar entre 1 y 10.')

class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    texto = models.TextField()
    calificacion = models.IntegerField(validators=[validar_calificacion])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion}/10"