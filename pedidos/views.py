from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

# Create your views here.

def catalogo(request):
    Producto = Producto.objects.all()
    texto = "Catalogo\n\n"
    for p in productos:
        texto += f"{p.nombre} - "
        texto += f"{p.categoria.nombre}\n"
    return HttpResponse(texto,
        content_type="text/plain charset=utf-8")