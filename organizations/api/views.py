from datetime import datetime
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from organizations.models import Organization, UserOrganization  # Update with your actual app name
from .serializers import OrganizationSerializer, OrgMembersSerializer  # Your organization serializer

# List all organizations (can be adjusted to only show joinable ones, etc.)
class OrganizationListView(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Organization.objects.filter(
            userorganization__user=self.request.user
        ).order_by(
            '-userorganization__last_accessed_at',
            '-userorganization__joined_at'
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
        
class OrgMembersListView(generics.ListAPIView):
    serializer_class = OrgMembersSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        org_id = self.kwargs.get('org_id')
        organization = get_object_or_404(Organization, id=org_id)
        return UserOrganization.objects.filter(organization=organization)
        

# Record that the current user has accessed (clicked) this org
class RecordOrgAccessView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, org_id):
        uo = get_object_or_404(
            UserOrganization,
            user=request.user,
            organization__id=org_id
        )
        # Use a naive datetime instead of timezone.now()
        uo.last_accessed_at = datetime.now()
        uo.save(update_fields=['last_accessed_at'])
        return Response(status=204)
    