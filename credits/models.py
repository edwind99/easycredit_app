from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Employ(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Product_type(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField() # quantity available
    product_type = models.ForeignKey(Product_type, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.product_type.name}"


class Credit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # Date the credit was created
    interest = models.DecimalField(max_digits=5, decimal_places=2)
    time_limit = models.IntegerField()  # Credit term in months

    STATUS_CHOICES = [
        ('STR', 'Start'),
        ('ACT', 'Active'),
        ('CMP', 'Completed'),
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='STR')

    def __str__(self):
        return f"Client: {self.client} - Product: {self.product}"
    
class Payment(models.Model):
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    STATUS_CHOICES = [
        ('PEN', 'Pending'),
        ('CMP', 'Completed'),
        ('DLY', 'Delayed'),
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')