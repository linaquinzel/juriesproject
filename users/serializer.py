from rest_framework import serializers
from .models import User, Events, Project, Evaluation_Criterion, Grades

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


class Evaluation_CriterionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Evaluation_Criterion
        fields = "__all__"

class ReportSerializer(serializers.ModelSerializer):
    class Meta():
        model = Evaluation_Criterion
        fields = ["evaluation_criterion"]

class VoteSerializer(serializers.ModelSerializer):
    class Meta():
        model = Grades
        fields = "__all__"
class RevoteSerializer(serializers.ModelSerializer):
    class Meta():
        model = Grades
        fields = ["grade"]

class EventLogSerializer(serializers.ModelSerializer):
    class Meta():
        model = Grades
        fields = ["grade", "author", "evaluation_criterion", "project", "event"]

class AddEventSerializer(serializers.ModelSerializer):
    class Meta():
        model = Events
        fields = ["name_of_event", "date_of_event"]