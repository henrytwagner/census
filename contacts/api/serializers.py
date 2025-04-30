# serializers.py
from rest_framework import serializers
from contacts.models import Contact
from django.contrib.auth.models import User

class ContactSerializer(serializers.ModelSerializer):
    # pull username off the linked User
    username = serializers.CharField(
        source='linked_profile.username',
        read_only=True,
        default=''
    )
    # pull profile image URL off the related UserProfile
    profile_image_url = serializers.CharField(
        source='linked_profile.profile.profile_image_url',
        read_only=True,
        default=''
    )

    class Meta:
        model = Contact
        fields = [
            'id',
            'user',
            'linked_profile',

            'username',
            'profile_image_url',

            'first_name',
            'last_name',
            'email',
            'phone',

            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class UnifiedContactSerializer(serializers.Serializer):
    contact_id = serializers.UUIDField(source='id', required=False, allow_null=True)
    user_id = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    username = serializers.CharField(source='linked_profile.username', required=False, allow_null=True)
    profile_image_url = serializers.CharField(
        source='linked_profile.profile.profile_image_url', required=False, allow_blank=True
    )
    bio = serializers.CharField(
        source='linked_profile.profile.bio', required=False, allow_blank=True
    )
    phone = serializers.CharField(required=False, allow_null=True)

    def get_user_id(self, obj):
        # Handle cases where obj is a dictionary
        if isinstance(obj, dict):
            return obj.get('linked_profile').id if obj.get('linked_profile') else None
        return obj.linked_profile.id if obj.linked_profile else None

    def get_first_name(self, obj):
        # Handle cases where obj is a dictionary
        if isinstance(obj, dict):
            return obj.get('linked_profile').first_name if obj.get('linked_profile') else None
        return obj.first_name or (obj.linked_profile.first_name if obj.linked_profile else None)

    def get_last_name(self, obj):
        # Handle cases where obj is a dictionary
        if isinstance(obj, dict):
            return obj.get('linked_profile').last_name if obj.get('linked_profile') else None
        return obj.last_name or (obj.linked_profile.last_name if obj.linked_profile else None)


