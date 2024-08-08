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

    marcas = Vehiculo.objects.values_list("marca", flat=True).distinct()
    vehiculos_nuevos = Vehiculo.objects.filter(tipo="0km")

    if marca:
        vehiculos_nuevos = vehiculos_nuevos.filter(marca__icontains=marca)
        modelos = Vehiculo.objects.filter(marca__icontains=marca).values_list(
            "modelo", flat=True).distinct()
    else:
        vehiculos_nuevos = Vehiculo.objects.none()
        modelos = Vehiculo.objects.none()

    if modelo:
        vehiculos_nuevos = vehiculos_nuevos.filter(modelo__icontains=modelo)

    contexto = {
        "marcas": marcas,
        "vehiculos": vehiculos_nuevos,
        "marca": marca,
        "modelo": modelo,
        "modelos": modelos
    }
    return render(request, "Home/nuevos.html", contexto)


def usados(request):
    marca = request.GET.get("marca", "")
    modelo = request.GET.get("modelo", "")

    marcas = Vehiculo.objects.values_list("marca", flat=True).distinct()
    vehiculos_usados = Vehiculo.objects.filter(tipo="Usado")

    if marca:
        vehiculos_usados = vehiculos_usados.filter(marca__icontains=marca)
        modelos = Vehiculo.objects.filter(marca__icontains=marca).values_list(
            "modelo", flat=True).distinct()
    else:
        vehiculos_usados = Vehiculo.objects.none()
        modelos = Vehiculo.objects.none()

    if modelo:
        vehiculos_usados = vehiculos_usados.filter(modelo__icontains=modelo)

    contexto = {
        "marcas": marcas,
        "vehiculos": vehiculos_usados,
        "marca": marca,
        "modelo": modelo,
        "modelos": modelos
    }
    return render(request, "Home/usados.html", contexto)
