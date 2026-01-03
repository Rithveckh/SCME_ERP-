from django.db import models
from django.contrib.auth.models import User
from tenants.models import Tenant
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    is_tenant_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username