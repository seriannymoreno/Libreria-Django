from django.db import models

# Create your models here.
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    codigo_rol = models.CharField(max_length=50)
    nombre_rol = models.CharField(max_length=100)

    class Meta:
        db_table = 'ROLES'

    def __str__(self):
        return self.nombre_rol

# 2. Modelo para los usuarios de la biblioteca
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)

    id_rol_fk = models.ForeignKey(
        Rol,
        on_delete=models.PROTECT,
        db_column='id_rol_fk',
        related_name='usuarios'
    )

    identificacion = models.CharField(max_length=50)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

# 3. Modelo para los autores
class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    nacionalidad = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    fecha_nac = models.DateField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'autor'

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

# 4. Modelo para las categorías
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nombre

# 5. Modelo para los libros
class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)

    id_categoria_fk = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        db_column='id_categoria_fk',
        related_name='libros'
    )

    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=50)
    anio_publicacion = models.PositiveSmallIntegerField(
        blank=True,
        null=True
    )
    editorial = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    num_paginas = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    autores = models.ManyToManyField(
        Autor,
        through='LibroAutor',
        related_name='libros'
    )

    class Meta:
        db_table = 'libro'

    def __str__(self):
        return self.titulo

# 6. Modelo intermedio para la relación libro-autor
class LibroAutor(models.Model):
    id_libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        db_column='id_libro'
    )

    id_autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        db_column='id_autor'
    )

    class Meta:
        db_table = 'libro_autor'
        constraints = [
            models.UniqueConstraint(
                fields=['id_libro', 'id_autor'],
                name='uq_libro_autor'
            )
        ]

    def __str__(self):
        return f'{self.id_libro} - {self.id_autor}'

# 7. Modelo para los préstamos
class Prestamo(models.Model):

    class Estado(models.TextChoices):
        ACTIVO = 'activo', 'Activo'
        DEVUELTO = 'devuelto', 'Devuelto'
        VENCIDO = 'vencido', 'Vencido'

    id_prestamo = models.AutoField(primary_key=True)

    id_libro = models.ForeignKey(
        Libro,
        on_delete=models.PROTECT,
        db_column='id_libro',
        related_name='prestamos'
    )

    id_usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        db_column='id_usuario',
        related_name='prestamos'
    )

    fecha_prestamo = models.DateTimeField(auto_now_add=True)

    fecha_limite = models.DateField(
        blank=True,
        null=True
    )

    fecha_devolucion = models.DateTimeField(
        blank=True,
        null=True
    )

    estado = models.CharField(
        max_length=10,
        choices=Estado.choices,
        default=Estado.ACTIVO
    )

    class Meta:
        db_table = 'prestamo'

    def __str__(self):
        return f'Préstamo {self.id_prestamo}: {self.id_libro}'
