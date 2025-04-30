from django.urls import path
from .views import (
    UserContactsListView,
    ContactCreateView,
    ContactRetrieveUpdateDeleteView,
    UnifiedContactView
)

urlpatterns = [
    path('', UserContactsListView.as_view(), name='user-contacts'),
    path('create/', ContactCreateView.as_view(), name='create-contact'),
    path('<uuid:pk>/', ContactRetrieveUpdateDeleteView.as_view(), name='contact-detail'),
    path('unified/', UnifiedContactView.as_view(), name='unified-contact'),
    path('unified/<uuid:contact_id>/', UnifiedContactView.as_view(), name='unified-contact-by-id'),
    path('unified/user/<int:user_id>/', UnifiedContactView.as_view(), name='unified-contact-by-user-id'),
]