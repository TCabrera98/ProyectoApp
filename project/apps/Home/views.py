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
    marcas = Vehiculo.objects.filter(tipo="0km").values_list(
        "marca", flat=True).distinct()
    if marca or modelo:
        vehiculos_nuevos = Vehiculo.objects.filter(tipo="0km")
        if marca:
            vehiculos_nuevos = vehiculos_nuevos.filter(marca__icontains=marca)
        if modelo:
            vehiculos_nuevos = vehiculos_nuevos.filter(
                modelo__icontains=modelo)
    else:
        vehiculos_nuevos = Vehiculo.objects.none()

    contexto = {
        "marcas": marcas,
        "vehiculos": vehiculos_nuevos,
        "marca": marca,
        "modelo": modelo,
    }
    return render(request, "Home/nuevos.html", contexto)


def usados(request):
    marca = request.GET.get("marca", "").strip()
    modelo = request.GET.get("modelo", "").strip()
    marcas = Vehiculo.objects.filter(tipo="Usado").values_list(
        "marca", flat=True).distinct()
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
        "marcas": marcas,
        "vehiculos": vehiculos_usados,
        "marca": marca,
        "modelo": modelo,
    }
    return render(request, "Home/usados.html", contexto)
