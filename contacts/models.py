from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid

# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # The owner who created this contact.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    # Optionally link to another User if the contact corresponds to an account.
    linked_profile = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='linked_contacts'
    )
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        full_name_contact = f"{self.first_name or ''} {self.last_name or ''}".strip()
        full_name_user = f"{self.user.first_name or ''} {self.user.last_name or ''}".strip()
        return full_name_user + "'s contact for " + full_name_contact or self.email or "Unnamed Contact"