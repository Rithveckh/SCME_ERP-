from django.contrib import admin
from django.urls import path

from accounts.views import (
    admin_dashboard,
    resident_dashboard,
    staff_dashboard
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path("resident-dashboard/", resident_dashboard, name="resident_dashboard"),
    path("staff-dashboard/", staff_dashboard, name="staff_dashboard"),
]
