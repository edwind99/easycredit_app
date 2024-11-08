from django.db import models

from clients.models import Client
from easycredit_app import settings
from products.models import Product

# Create your models here.

class Credit(models.Model):
    STATUSES = {
        "pending": "Pending",
        "approved": "Approved",
        "rejected": "Rejected",
        "active": "Active",
        "completed": "Completed",
        "past_due": "Past Due"
    }
    status = models.CharField(max_length=55, choices=STATUSES)
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    installments = models.SmallIntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    # interest_rate = models.ForeignKey(InterestRate, default=0.0, on_delete=models.RESTRICT)
    start_date = models.DateField(null=False)
    estimated_end_date = models.DateField
    application_date = models.DateField(null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Client: {self.client} - Product: {self.product}"
    
class Payment(models.Model):
    

    STATUSES = {
        'pending': 'Pending',
        'completed': 'Completed',
        'failed': 'Failed'
    }

    TYPES = {
        'regular': 'Regular Payment',
        'advance': 'Advance Payment'
    }
    credit = models.ForeignKey(Credit, on_delete=models.RESTRICT)
    date = models.DateTimeField(null=False)
    type = models.CharField(max_length=55, choices=TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    status = models.CharField(max_length=55, choices=STATUSES)
    overdue = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.credit} - {self.date} - {self.amount} - {self.status}'