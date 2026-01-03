from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.signals import user_logged_in
from audit.models import AuditLog

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    if hasattr(user, 'userprofile') and user.userprofile.tenant:
        AuditLog.objects.create(
            tenant=user.userprofile.tenant,
            user=user,
            action="User logged in"
        )