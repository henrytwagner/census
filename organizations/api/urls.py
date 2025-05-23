from django.urls import path
from .views import (
    OrganizationListView,
    OrganizationCreateView,
    OrganizationRetrieveUpdateDeleteView,
    OrgMembersListView,
    RecordOrgAccessView,
)

urlpatterns = [
    path('', OrganizationListView.as_view(), name='organization-list'),
    path('create/', OrganizationCreateView.as_view(), name='organization-create'),
    path('<uuid:pk>/', OrganizationRetrieveUpdateDeleteView.as_view(), name='organization-detail'),
    path('<uuid:org_id>/members/', OrgMembersListView.as_view(), name='organization-members-list'),
    path('<uuid:org_id>/access/', RecordOrgAccessView.as_view(), name='org-access'),
]