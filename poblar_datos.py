from biblioteca.models import Autor, Libro, Resena

# Crear autores
autor1 = Autor.objects.create(
    nombre="Gabriel Garcia Marquez",
    fecha_nacimiento="1927-03-06",
    nacionalidad="Colombiana"
)

autor2 = Autor.objects.create(
    nombre="Isabel Allende",
    fecha_nacimiento="1942-08-02",
    nacionalidad="Chilena"
)

autor3 = Autor.objects.create(
    nombre="Mario Vargas Llosa",
    fecha_nacimiento="1936-03-28",
    nacionalidad="Peruana"
)

autor4 = Autor.objects.create(
    nombre="Julio Cortazar",
    fecha_nacimiento="1914-08-26",
    nacionalidad="Argentina"
)

autor5 = Autor.objects.create(
    nombre="Laura Esquivel",
    fecha_nacimiento="1950-09-30",
    nacionalidad="Mexicana"
)

autor6 = Autor.objects.create(
    nombre="Jorge Luis Borges",
    fecha_nacimiento="1899-08-24",
    nacionalidad="Argentina"
)

# Crear libros
libro1 = Libro.objects.create(
    titulo="Cien años de soledad",
    autor=autor1,
    fecha_publicacion="1967-06-05",
    resumen="Novela emblemática del realismo mágico en Latinoamérica, que narra la historia de la familia Buendía."
)

libro2 = Libro.objects.create(
    titulo="La casa de los espíritus",
    autor=autor2,
    fecha_publicacion="1982-01-01",
    resumen="Relato de varias generaciones de una familia chilena donde se mezcla lo mágico y lo político."
)

libro3 = Libro.objects.create(
    titulo="La ciudad y los perros",
    autor=autor3,
    fecha_publicacion="1963-10-10",
    resumen="Novela que retrata la vida de los cadetes en un colegio militar en Lima."
)

libro4 = Libro.objects.create(
    titulo="Rayuela",
    autor=autor4,
    fecha_publicacion="1963-06-28",
    resumen="Obra fundamental del boom latinoamericano que propone una lectura no lineal."
)

libro5 = Libro.objects.create(
    titulo="Como agua para chocolate",
    autor=autor5,
    fecha_publicacion="1989-09-01",
    resumen="Novela que mezcla recetas, amor y tradiciones mexicanas en un ambiente mágico."
)

libro6 = Libro.objects.create(
    titulo="Ficciones",
    autor=autor6,
    fecha_publicacion="1944-01-01",
    resumen="Colección de cuentos filosóficos que exploran laberintos, espejos y realidades múltiples."
)

# Crear reseñas
resena1 = Resena.objects.create(
    libro=libro1,
    texto="Una obra maestra del realismo mágico. Inolvidable.",
    calificacion=5.0
)

resena2 = Resena.objects.create(
    libro=libro2,
    texto="Un relato conmovedor y mágico de generaciones familiares.",
    calificacion=4.5
)

resena3 = Resena.objects.create(
    libro=libro3,
    texto="Una crítica dura pero necesaria sobre la vida militar.",
    calificacion=4.0
)

resena4 = Resena.objects.create(
    libro=libro4,
    texto="Una experiencia de lectura única y desafiante.",
    calificacion=4.5
)

resena5 = Resena.objects.create(
    libro=libro5,
    texto="Una historia encantadora que combina amor, cocina y tradiciones.",
    calificacion=5.0
)

resena6 = Resena.objects.create(
    libro=libro6,
    texto="Cada cuento es un universo en sí mismo, absolutamente brillante.",
    calificacion=5.0
)

resena7 = Resena.objects.create(
    libro=libro1,
    texto="El mejor libro que he leído en mi vida. Totalmente recomendable.",
    calificacion=5.0
)

resena8 = Resena.objects.create(
    libro=libro2,
    texto="Una buena historia pero por momentos se siente lenta.",
    calificacion=2.9
)

resena9 = Resena.objects.create(
    libro=libro5,
    texto="Interesante mezcla de cocina y romance, aunque algo predecible.",
    calificacion=3.5
)

resena10 = Resena.objects.create(
    libro=libro3,
    texto="No logré conectar con los personajes, me costó terminarlo.",
    calificacion=2.0
)

resena11 = Resena.objects.create(
    libro=libro6,
    texto="Demasiado abstracto para mi gusto, me pareció confuso.",
    calificacion=1.5
)
