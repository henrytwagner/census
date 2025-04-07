from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from .api.serializers import ContactSerializer

# Create your views here.
def index(request):
    return HttpResponse("Contacts App")
