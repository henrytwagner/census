from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserContactsListView.as_view(), name="contacts"),
]
