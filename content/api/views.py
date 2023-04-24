from rest_framework import viewsets

from .serializers import *


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().order_by("id")


class TechnologyViewSet(viewsets.ModelViewSet):
    serializer_class = TechnologySerializer
    queryset = Technology.objects.all().order_by("id")


class AboutViewSet(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all().order_by('-id')


class ContactViewSets(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all().order_by('-id')
