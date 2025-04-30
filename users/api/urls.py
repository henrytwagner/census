from django.urls import path
from .views import (
    MeRetrieveUpdateView,
    RegisterView,
    PublicProfileView
)

urlpatterns = [
    path('me/', MeRetrieveUpdateView.as_view(), name='me'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:id>/', PublicProfileView.as_view(), name='public_profile'),]