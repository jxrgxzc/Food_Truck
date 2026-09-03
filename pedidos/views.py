from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

# Create your views here.

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, "pedidos/catalogo.html",  {"productos":productos})