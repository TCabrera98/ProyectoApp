from django.shortcuts import render
from . import models


def index(request):
    vehiculos = models.Vehiculo.objects.all()
    return render(request, "vehiculo/index.html", {"vehiculos": vehiculos})
