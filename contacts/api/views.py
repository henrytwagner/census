from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from contacts.models import Contact
from django.contrib.auth.models import User
from .serializers import ContactSerializer, UnifiedContactSerializer

# List contacts for the current user
class UserContactsListView(generics.ListAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


# Create a new contact for the current user
class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Retrieve Update or Delete a contact
class ContactRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return Contact.objects.get(id=self.kwargs['pk'], user=self.request.user)
        except Contact.DoesNotExist:
            raise NotFound("Contact not found")

class UnifiedContactView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        contact_id = kwargs.get('contact_id')
        user_id = kwargs.get('user_id')

        if contact_id:
            # Fetch the contact by ID
            contact = Contact.objects.filter(id=contact_id, user=request.user).first()
            if not contact:
                return Response({"detail": "Contact not found."}, status=404)
            serializer = UnifiedContactSerializer(contact)
        elif user_id:
            # Fetch the user by ID
            user = User.objects.filter(id=user_id).first()
            if not user:
                return Response({"detail": "User not found."}, status=404)

            # Fetch the contact linked to the user
            contact = Contact.objects.filter(linked_profile=user, user=request.user).first()

            # If no contact exists, create a temporary object for serialization
            if contact:
                serializer = UnifiedContactSerializer(contact)
            else:
                serializer = UnifiedContactSerializer({"linked_profile": user})
        else:
            return Response({"detail": "Invalid request."}, status=400)

        return Response(serializer.data)