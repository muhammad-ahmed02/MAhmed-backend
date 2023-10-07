from rest_framework.serializers import ModelSerializer

from content.models import *


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        depth = 1


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


class LearningSerializer(ModelSerializer):
    class Meta:
        model = Learning
        fields = "__all__"
