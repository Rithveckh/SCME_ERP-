from django.db import models
from community.models import Resident
from tenants.models import Tenant

# Create your models here.
class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('CLOSED', 'Closed'),
    ]

    request_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )
    resident = models.ForeignKey(
        Resident,
        on_delete=models.CASCADE
    )
    service_type = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_type}"
