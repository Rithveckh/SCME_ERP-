from django.contrib import admin
from .models import MaintenanceBill, Payment
# Register your models here.
admin.site.register(MaintenanceBill)
admin.site.register(Payment)