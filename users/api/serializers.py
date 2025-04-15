from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import UserProfile

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
        
class MeSerializer(serializers.ModelSerializer):
    profile_image_url = serializers.CharField(source='profile.profile_image_url', read_only=True)
    bio = serializers.CharField(source='profile.bio', read_only=True)
    # Add additional profile fields here if needed

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'profile_image_url',
            'bio'
        ]