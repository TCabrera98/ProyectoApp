from django.contrib import admin
from .models import Vehiculo, VehiculoImagen

# Personalización del sitio de administración
admin.site.site_header = "Cabrera Automotores"
admin.site.site_title = "Cabrera Automotores"


class VehiculoImagenInline(admin.TabularInline):
    model = VehiculoImagen
    extra = 1
    can_delete = True


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de vehículos
    list_display = ('marca', 'modelo', 'año',
                    'kilometraje')

    # Campos por los que se puede buscar en el panel de administración
    search_fields = ('marca', 'modelo', 'año', 'kilometraje')

    # Campos por los que se puede filtrar en el panel de administración
    list_filter = ('marca', 'modelo', 'año', 'color')

    # Agregar imágenes al panel de administración
    inlines = [VehiculoImagenInline]
