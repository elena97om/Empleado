from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50) #puede estar vacío blank=True
    shor_name = models.CharField('Nombre corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name']
        unique_together = ('name', 'shor_name') #para no registrar una combinación similar entre nombre y shor_name

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name