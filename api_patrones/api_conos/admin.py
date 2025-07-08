

from django.contrib import admin
from .models import PedidoCono

@admin.register(PedidoCono)
class PedidoConoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'variante', 'tamanio_cono', 'fecha_pedido')
    list_filter = ('variante', 'tamanio_cono', 'fecha_pedido')
    search_fields = ('cliente',)

# Register your models here.
