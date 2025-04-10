from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from organizations.models import Organization, UserOrganization  # Update with your actual app name
from .serializers import OrganizationSerializer  # Your organization serializer

# List all organizations (can be adjusted to only show joinable ones, etc.)
class OrganizationListView(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Optional: customize to show only public/orgs user can see
        return Organization.objects.filter(
            userorganization__user=self.request.user
        )


# Create a new organization
class OrganizationCreateView(generics.CreateAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Optional: attach creator as an admin in UserOrganization model
        return serializer.save()


# Retrieve, update, or delete a specific organization
class OrganizationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return Organization.objects.get(id=self.kwargs['pk'])
        except Organization.DoesNotExist:
            raise NotFound("Organization not found")
        
        
    