from rest_framework import serializers
from .models import User, Events, Project, Grades

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = "__all__"


class EventsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Events
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = Project
        fields = "__all__"


class GradesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Grades
        fields = "__all__"