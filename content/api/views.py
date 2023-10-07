from rest_framework import viewsets

from .serializers import *


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().order_by("id")
    http_method_names = ['get']


class TechnologyViewSet(viewsets.ModelViewSet):
    serializer_class = TechnologySerializer
    queryset = Technology.objects.all().order_by("id")
    http_method_names = ['get']


class AboutViewSet(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all().order_by('-id')
    http_method_names = ['get']


class ContactViewSets(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all().order_by('-id')
    http_method_names = ['post']


class LearningViewSets(viewsets.ModelViewSet):
    serializer_class = LearningSerializer
    queryset = Learning.objects.all().order_by('-id')
    http_method_names = ['get']
