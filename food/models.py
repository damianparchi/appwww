from unicodedata import decimal
from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=120)
    priceSMALL = models.DecimalField(max_digits=4, decimal_places=2)
    priceBIG = models.DecimalField(max_digits=4, decimal_places=2)

class Kebab(models.Model):
    name = models.CharField(max_length=120)
    priceSMALL = models.DecimalField(max_digits=4, decimal_places=2)
    priceBIG = models.DecimalField(max_digits=4, decimal_places=2)

