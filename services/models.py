from django.db import models


class NivelAmbito(models.Model):
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = True


# Create your models here.
class camposReporte(models.Model):
    nivel = models.ForeignKey(NivelAmbito)
    descripcion = models.CharField(max_length=255)
    islabel = models.IntegerField(default=0)
    order = models.IntegerField()
    db_field = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        managed = True
