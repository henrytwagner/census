from django.urls import path
from .views import (
    UserContactsListView,
    ContactCreateView,
    ContactRetrieveUpdateDeleteView
)

urlpatterns = [
    path('', UserContactsListView.as_view(), name='user-contacts'),
    path('create/', ContactCreateView.as_view(), name='create-contact'),
    path('<uuid:pk>/', ContactRetrieveUpdateDeleteView.as_view(), name='contact-detail'),
]