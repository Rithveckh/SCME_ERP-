from django.db import models
from service.models import ServiceRequest
from tenants.models import Tenant

# Create your models here.
class InventoryItem(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=20)
    reorder_level = models.PositiveIntegerField()

    def __str__(self):
        return self.item_name


class Asset(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    last_maintenance = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, default='Working')

    def __str__(self):
        return self.asset_name

    
class InventoryUsage(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity_used = models.PositiveIntegerField()
