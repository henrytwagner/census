from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import UserProfile
from rest_framework.validators import UniqueValidator
from contacts.models import Contact



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
    profile_image_url = serializers.CharField(source='profile.profile_image_url', allow_blank=True, required=False)
    bio = serializers.CharField(source='profile.bio', allow_blank=True, required=False)
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
        read_only_fields = ['id', 'username']
        
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        profile=instance.profile
        for attr, value in profile_data.items():
            setattr(profile, attr, value)
        profile.save()
        return instance
    
class RegisterUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
          UniqueValidator(
            queryset=User.objects.all(),
            message="That username is already taken."
          )
        ]
    )
    
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, label="Confirm password", min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password2": "Passwords must match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
    

    
class PublicProfileSerializer(serializers.ModelSerializer):
    """Serialize a user's public profile + whether the current user
       already has a private contact for them."""
    profile_image_url = serializers.CharField(
        source='profile.profile_image_url', read_only=True, allow_blank=True
    )
    bio = serializers.CharField(
        source='profile.bio', read_only=True, allow_blank=True
    )
    my_contact = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email',
            'first_name', 'last_name',
            'profile_image_url', 'bio',
            'my_contact',
        ]
        read_only_fields = ['id', 'username', 'email', 
                            'first_name', 'last_name',
                            'profile_image_url', 'bio', 'my_contact']

    def get_my_contact(self, user):
        """If the requesting user already has a Contact linked to this User, return it."""
        request_user = self.context['request'].user
        contact = Contact.objects.filter(
            owner=request_user,
            linked_profile=user
        ).first()
        if not contact:
            return None
        return {
            'id':         str(contact.id),
            'first_name': contact.first_name,
            'last_name':  contact.last_name,
            # add any other private‐only fields you want surfaced
        }