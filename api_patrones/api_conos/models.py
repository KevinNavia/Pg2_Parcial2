from django.db import models
from django.core.exceptions import ValidationError

class PedidoCono(models.Model):
    VARIANTES = [
        ('Carnívoro', 'Carnívoro'),
        ('Vegetariano', 'Vegetariano'),
        ('Saludable', 'Saludable'),
    ]
    TOPPINGS_VALIDOS = {'queso_extra', 'papas_al_hilo', 'salchicha_extra'}  # Si agregas más, inclúyelos aquí

    cliente = models.CharField(max_length=255)
    variante = models.CharField(max_length=20, choices=VARIANTES)
    toppings = models.JSONField(default=list, blank=True, null=True)
    tamanio_cono = models.CharField(
        max_length=20,
        choices=[('Pequeño','Pequeño'),('Mediano','Mediano'),('Grande','Grande')]
    )
    fecha_pedido = models.DateField(auto_now_add=True)

    def clean(self):
        super().clean()
        # validar toppings: debe ser lista y cada elemento en TOPPINGS_VALIDOS
        if self.toppings is not None:
            if not isinstance(self.toppings, list):
                raise ValidationError({'toppings': 'Debe ser una lista de toppings.'})
            invalid = [t for t in self.toppings if t not in self.TOPPINGS_VALIDOS]
            if invalid:
                raise ValidationError({
                    'toppings': f'Toppings inválidos: {invalid}. Solo se permiten {list(self.TOPPINGS_VALIDOS)}'
                })

    def save(self, *args, **kwargs):
        self.full_clean()  # fuerza validación del modelo al guardarse
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente} ({self.variante})"

# Create your models here.
