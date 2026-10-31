from django.core.management.base import BaseCommand
from catalogo.models import Categoria, Autor, Libro

class Command(BaseCommand):
    help = 'Carga registros iniciales en la base de datos'

    def handle(self, *args, **options):
        # --- Categoria 1 y Autor 1 (Original) ---
        cat_prog = Categoria.objects.create(
            nombre="Programación",
            descripcion="Libros de desarrollo de software"
        )
        autor_carlos = Autor.objects.create(
            nombres="Carlos",
            apellidos="Pérez",
            nacionalidad="Colombiana"
        )
        libro1 = Libro.objects.create(
            id_categoria_fk=cat_prog,
            titulo="Introducción a Python",
            isbn="9780000000001",
            anio_publicacion=2025,
            editorial="Editorial Académica",
            num_paginas=250
        )
        libro1.autores.add(autor_carlos)

        # --- Categoria 2 y Autor 2 (Nuevo Registro 1) ---
        cat_bd = Categoria.objects.create(
            nombre="Bases de Datos",
            descripcion="Diseño y administración de bases de datos"
        )
        autor_maria = Autor.objects.create(
            nombres="María",
            apellidos="Gómez",
            nacionalidad="Mexicana"
        )
        libro2 = Libro.objects.create(
            id_categoria_fk=cat_bd,
            titulo="SQL para Principiantes",
            isbn="9780000000002",
            anio_publicacion=2024,
            editorial="Tech Books",
            num_paginas=310
        )
        libro2.autores.add(autor_maria)

        # --- Categoria 3 y Autor 3 (Nuevo Registro 2) ---
        cat_web = Categoria.objects.create(
            nombre="Desarrollo Web",
            descripcion="Frontend y Backend para la web"
        )
        autor_juan = Autor.objects.create(
            nombres="Juan",
            apellidos="Rodríguez",
            nacionalidad="Argentina"
        )
        libro3 = Libro.objects.create(
            id_categoria_fk=cat_web,
            titulo="Django y Web APIs",
            isbn="9780000000003",
            anio_publicacion=2026,
            editorial="Editorial Código",
            num_paginas=420
        )
        libro3.autores.add(autor_juan)

        self.stdout.write(self.style.SUCCESS('¡Todos los registros se crearon exitosamente!'))