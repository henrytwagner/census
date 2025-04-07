from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import UserProfile
from organizations.models import Organization, UserOrganization, ContactOrganization
from contacts.models import Contacts

User = get_user_model()

# Serializer for built-in User.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Expose common fields; password handling should be done with create_user.
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']

# Serializer for the user profile.
class UserProfileSerializer(serializers.ModelSerializer):
    # Optionally nest user info here if needed.
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'profile_image_url', 'bio']
