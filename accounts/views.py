from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from community.models import Resident
from service.models import ServiceRequest
from billing.models import MaintenanceBill


# =========================
# ADMIN DASHBOARD
# =========================
@login_required
def admin_dashboard(request):
    context = {
        "total_residents": Resident.objects.count(),
        "total_requests": ServiceRequest.objects.count(),
        # FIX: field name is bill_status, NOT status
        "pending_bills": MaintenanceBill.objects.filter(bill_status="PENDING").count(),
    }
    return render(request, "admin_dashboard.html", context)


# =========================
# RESIDENT DASHBOARD
# =========================
@login_required
def resident_dashboard(request):
    # FIX: Resident has NO `user` field
    # We safely link Resident ↔ User using email
    resident = Resident.objects.filter(email=request.user.email).first()

    context = {
        "requests": ServiceRequest.objects.filter(resident=resident) if resident else [],
        "bills": MaintenanceBill.objects.filter(resident=resident) if resident else [],
    }
    return render(request, "resident_dashboard.html", context)


# =========================
# STAFF DASHBOARD
# =========================
@login_required
def staff_dashboard(request):
    # FIX: ServiceRequest uses `status` (this one is correct)
    context = {
        "open_requests": ServiceRequest.objects.filter(status="OPEN")
    }
    return render(request, "staff_dashboard.html", context)
