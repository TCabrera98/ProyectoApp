from django.shortcuts import render
from vehiculo.models import Vehiculo  # Importa el modelo Vehiculo


def index(request):
    vehiculos = Vehiculo.objects.all()  # Obtiene todos los vehículos
    return render(request, "Home/index.html", {"vehiculos": vehiculos})


def nosotros(request):
    return render(request, "Home/nosotros.html")


def nuevos(request):
    marca = request.GET.get("marca", "").strip()
    modelo = request.GET.get("modelo", "").strip()
    marcas = ["Toyota", "Volkswagen", "Ford",
              "Chevrolet", "Fiat", "Renault", "Peugeot", "Honda"]

    vehiculos_nuevos = Vehiculo.objects.filter(tipo="0km")

    if marca:
        vehiculos_nuevos = vehiculos_nuevos.filter(marca__icontains=marca)
    if modelo:
        vehiculos_nuevos = vehiculos_nuevos.filter(modelo__icontains=modelo)
    if marca:
        modelos = Vehiculo.objects.filter(marca__icontains=marca).values_list(
            "modelo", flat=True).distinct()
    else:
        modelos = Vehiculo.objects.none()

    contexto = {
        "marcas": marcas,
        "vehiculos": vehiculos_nuevos,
        "marca": marca,
        "modelo": modelo,
        "modelos": modelos
    }
    return render(request, "Home/nuevos.html", contexto)


def usados(request):
    marca = request.GET.get("marca", "").strip()
    modelo = request.GET.get("modelo", "").strip()

    if marca or modelo:
        vehiculos_usados = Vehiculo.objects.filter(tipo="Usado")
        if marca:
            vehiculos_usados = vehiculos_usados.filter(marca__icontains=marca)
        if modelo:
            vehiculos_usados = vehiculos_usados.filter(
                modelo__icontains=modelo)
    else:
        vehiculos_usados = Vehiculo.objects.none()

    contexto = {
        "vehiculos": vehiculos_usados,
        "marca": marca,
        "modelo": modelo,
    }
    return render(request, "Home/usados.html", contexto)
