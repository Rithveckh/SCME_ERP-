from django.contrib import admin
from .models import InventoryItem, Asset, InventoryUsage
# Register your models here.
admin.site.register(InventoryItem)
admin.site.register(Asset)
admin.site.register(InventoryUsage)