from django.db import models

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField() # quantity available
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    def __str__(self):
        return f"{self.name} - {self.product_type}"