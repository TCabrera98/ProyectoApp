from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "Home"

urlpatterns = [
    path("", views.index, name="home"),
    path("nuevos/", views.nuevos, name="nuevos"),
    path("usados/", views.usados, name="usados"),
    path("nosotros/", views.nosotros, name="nosotros"),
]

urlpatterns += staticfiles_urlpatterns()
