from django.db import models
from tenants.models import Tenant

# Create your models here.
class Resident(models.Model):
    resident_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    flat_no = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return f"{self.name} ({self.flat_no})"