from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre= models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT,
        related_name="productos",
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]
        
    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    ESTADOS =[
        ("pendiente","Pendiente"),
        ("entregado","Entregado"),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["estado"]

    def __str__(self):
        return f"Pedido (self.id)"

class DetallePedido(models.Model):
    pedido = models.ForeignKey( 
    Pedido, 
    on_delete=models.CASCADE,
    related_name="detalles",
    )
    producto = models.ForeignKey(
    Producto, 
    on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=1)
    subtotal = models.IntegerField()

    class Meta:
        verbose_name = "DetallePedido"
        verbose_name_plural = "DetallePedidos"
        ordering = ["cantidad"]

    def __str__(self):
        return f"(self.cantidad) = (self.productos)"