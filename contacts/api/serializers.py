from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import UserProfile
from organizations.models import Organization, UserOrganization, ContactOrganization
from contacts.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'user',
            'linked_profile',
            'first_name',
            'last_name',
            'email',
            'phone',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']