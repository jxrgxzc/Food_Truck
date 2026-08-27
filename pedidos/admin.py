from django.contrib import admin
from .models import Categoria, Producto, Cliente, Pedido, DetallePedido

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre","precio","categoria")
    search_fields = ("nombre",)
    list_filter = ("categoria",)
    ordering = ("nombre",)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre","telefono")
    search_fields = ("nombre",)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("ESTADOS","cliente","fecha","estado")
    search_fields = ("ESTADOS",)

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido","producto","cantidad","subtotal")
    search_fields = ("pedido",)