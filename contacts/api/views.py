from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from contacts.models import Contact
from .serializers import ContactSerializer

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