from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "Home"

urlpatterns = [
    path("", views.index, name="home"),
    path("nuevos/", views.nuevos, name="nuevos"),
    path("usados/", views.usados, name="usados"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("vehiculo_imagenes/<int:vehiculo_id>/",
         views.vehiculo_imagenes, name="vehiculo_imagenes"),
]

urlpatterns += staticfiles_urlpatterns()
