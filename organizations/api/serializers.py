from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import UserProfile
from organizations.models import Organization, UserOrganization, ContactOrganization
from contacts.models import Contact

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'photo_url', 'bio', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class UserOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrganization
        fields = ['user', 'organization', 'role', 'joined_at']
        read_only_fields = ['joined_at']

class ContactOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactOrganization
        fields = ['contact', 'organization']