from django.db import models
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL
# Create your models here.

class TypeProduct(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=128)

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    stock = models.IntegerField()
    typeId = models.ForeignKey(TypeProduct, on_delete=PROTECT)