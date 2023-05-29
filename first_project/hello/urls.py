#importar una bliblioteca administradora de rutas
from django.urls import path

#importando vistas
from . import views

#declarandoo las rutas vistas
#urlpatterns = [
    #get/hello/
#    path("", views.index, name="index"),
    #get/hello/author
#    path("author/", views.author, name="author"),
# ] 

# from django.urls import path
# # Importando views del directorio actual
# from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("author/", views.author, name="luis"),
#     path("<str:name>", views.greet, name="greet")
# ]

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def author(request):
    return HttpResponse("Hello Author 👨‍🎤")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!!!")