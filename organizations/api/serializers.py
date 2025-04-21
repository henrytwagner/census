from rest_framework import serializers
from django.contrib.auth import get_user_model
from organizations.models import Organization, UserOrganization, ContactOrganization

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
        
class OrgMembersSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='user.id')
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    # If there’s no profile, you can return an empty string
    profile_image_url = serializers.CharField(source='user.profile.profile_image_url', default='', allow_blank=True)
    role = serializers.CharField()

    class Meta:
        model = UserOrganization
        fields = ['id', 'username', 'first_name', 'last_name', 'profile_image_url', 'role']