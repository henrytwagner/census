# serializers.py
from rest_framework import serializers
from contacts.models import Contact

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