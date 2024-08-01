from django.db import models


class Vehiculo(models.Model):
    """ Clase para almacenar los datos de los vehiculos """
    tipo = [
        ("0km", "0km"),
        ("Usado", "Usado"),
    ]

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    año = models.IntegerField(null=True, blank=True)
    kilometraje = models.IntegerField(null=True, default=0)
    color = models.CharField(max_length=50, null=True, blank=True)
    tipo = models.CharField(max_length=50, choices=tipo, default="0km")

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.año}"

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"


class VehiculoImagen(models.Model):
    """ Clase para almacenar las imagenes de los vehiculos """
    vehiculo = models.ForeignKey(
        Vehiculo, related_name="imagenes", on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to="vehiculo/imagenes/")

    def __str__(self):
        return f"{self.vehiculo} {self.imagen}"
