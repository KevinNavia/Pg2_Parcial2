from rest_framework import serializers
from .models import PedidoCono

class PedidoConoSerializer(serializers.ModelSerializer):
    precio_final = serializers.SerializerMethodField()
    ingredientes_finales = serializers.SerializerMethodField()

    class Meta:
        model = PedidoCono
        fields = [
            'id', 'cliente', 'variante', 'toppings',
            'tamanio_cono', 'fecha_pedido',
            'precio_final', 'ingredientes_finales'
        ]
        read_only_fields = ('fecha_pedido', 'precio_final', 'ingredientes_finales')

    def get_precio_final(self, obj):
        # lógica de precios ejemplo:
        precios = {'Pequeño': 3, 'Mediano': 5, 'Grande': 7}
        base = precios.get(obj.tamanio_cono, 0)
        extra = len(obj.toppings) * 0.5
        return base + extra

    def get_ingredientes_finales(self, obj):
        # lógica basada en variante + toppings
        base_ingredientes = {
            'Carnívoro': ['carne', 'queso'],
            'Vegetariano': ['verduras', 'queso'],
            'Saludable': ['frutas', 'yogur']
        }
        return base_ingredientes[obj.variante] + obj.toppings
