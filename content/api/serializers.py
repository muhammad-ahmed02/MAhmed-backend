from rest_framework.serializers import ModelSerializer

from content.models import *


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TechnologySerializer(ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
