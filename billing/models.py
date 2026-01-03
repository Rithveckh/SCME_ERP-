from django.db import models
from community.models import Resident
from tenants.models import Tenant
# Create your models here.
class MaintenanceBill(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    bill_month = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    bill_status = models.CharField(max_length=20, default='Unpaid')

    
class Payment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    bill = models.ForeignKey(MaintenanceBill, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=30)

