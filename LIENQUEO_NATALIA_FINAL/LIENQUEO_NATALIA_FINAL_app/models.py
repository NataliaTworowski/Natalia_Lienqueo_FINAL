from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    ESTADOS = [
        ('RESERVADO', 'Reservado'), 
        ('COMPLETADA', 'Completada'), 
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten')
    ]

    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_inscripcion = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    hora_inscripcion = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
