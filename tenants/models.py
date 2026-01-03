from django.db import models

# Create your models here.
class Tenant(models.Model):
    tenant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    status = models.CharField(
        max_length=20,
        default='Active'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name