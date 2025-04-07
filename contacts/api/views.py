from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from contacts.models import Contact
from .serializers import ContactSerializer

# Create your views here.

class UserContactsListView(generics.ListAPIView):
    """
    API view that returns all contacts for the logged-in user.
    """
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter contacts for the authenticated user.
        return Contact.objects.filter(user=self.request.user)
