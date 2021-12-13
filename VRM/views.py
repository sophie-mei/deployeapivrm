from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer

class PersonsView(viewsets.ModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer

# Create your views here.
