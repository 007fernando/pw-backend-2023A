#importar una bliblioteca administradora de rutas
from django.urls import path

#importando vistas
from . import views

#declarandoo las rutas vistas
urlpatterns = [
    #get/hello/
    path("", views.index, name="index"),
    #get/hello/author
    path("author/", views.author, name="author"),
    ] 
