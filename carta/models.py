from django.db import models

# Create your models here.

class Item(models.Model):
    '''names, prices, stock and descriptions.'''
    PRODUCT_CATEG_CHOICES = {
        'B': 'Bebida',
        'C': 'Comida',
        'M': 'Miscelaneo',
        }
    
    name = models.CharField(max_length=80)
    prize = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True,)
    categ = models.CharField(
        choices=PRODUCT_CATEG_CHOICES,
        default='B',
        blank=False,
        max_length=10,
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["categ", "name"]
