from django.contrib import admin
from .models import Organization, UserOrganization, ContactOrganization

# Register your models here.
admin.site.register(Organization)
admin.site.register(UserOrganization)
admin.site.register(ContactOrganization)
