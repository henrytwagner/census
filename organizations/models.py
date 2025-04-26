from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from contacts.models import Contact
import uuid


# Create your models here.
class Organization(models.Model):
    # Using a UUID as primary key.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    photo_url = models.URLField(max_length=512, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class UserOrganization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default='active')  # e.g., active, inactive
    joined_at = models.DateTimeField(auto_now_add=True)
    last_accessed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'organization')

    def __str__(self):
        return f"{self.user.username} in {self.organization.name}"

class ContactOrganization(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('contact', 'organization')

    def __str__(self):
        return f"{self.contact} in {self.organization.name}"

