from django.db import models

# Create your models here.

class Client(models.Model):
    identifier = models.CharField(max_length=127, null=False, unique=True)
    first_name = models.CharField(max_length=511, null=False)
    last_name = models.CharField(max_length=511, null=False)
    
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
