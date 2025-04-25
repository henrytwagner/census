from django.urls import path
from .views import (
    MeRetrieveUpdateView,
    RegisterView
)

urlpatterns = [
    path('me/', MeRetrieveUpdateView.as_view(), name='me'),
    path('register/', RegisterView.as_view(), name='register'),
]