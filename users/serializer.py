from multiprocessing import Event
from rest_framework import serializers
from .models import User, Events, Project, Evaluation_Criterion, Grades
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = "__all__"


class EventsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Events
        fields = ["name_of_event", "date_of_event", "start_event"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = Project
        fields = ["event", "name_of_project", "speaker_name"]


class Evaluation_CriterionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Evaluation_Criterion
        fields = "__all__"

class ReportSerializer(serializers.ModelSerializer):
    class Meta():
        model = Evaluation_Criterion
        fields = ["evaluation_criterion"]

class VoteSerializer(serializers.Serializer):
    project = serializers.IntegerField(read_only=True)
    evaluation_criterion = serializers.IntegerField(read_only=True)
    author = serializers.IntegerField(read_only=True) 
    grade = serializers.ChoiceField(choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")])
    
    def create(self, validated_data):
        projects = validated_data.get("project")
        if Project.objects.filter(pk=projects).only("start_project"):
            grade = Grades.objects.create(**validated_data)
            return grade
        else:
            return Response()
        
    def update(self, instance, validated_data):
        datas = validated_data.get("project")
        instance.project = validated_data.get("project")
        instance.evaluation_criterion = validated_data.get(
            "evaluation_criterion", instance.evaluation_criterion
        )
        instance.author = validated_data.get("author")
        instance.grade = validated_data.get("grade", instance.grade)
        instance.save()
        if Project.objects.filter(pk=datas).only("start_project"):
            return instance
    

class RevoteSerializer(serializers.ModelSerializer):
    class Meta():
        model = Grades
        fields = ["grade"]

class EventLogSerializer(serializers.ModelSerializer):
    class Meta():
        model = Grades
        fields = ["grade", "author", "evaluation_criterion", "project"]

class EventHistorySerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    class Meta():
        
        model = Grades
        fields = ["grade", "event", "author", "project"]

class AddEventSerializer(serializers.ModelSerializer):
    class Meta():
        model = Events
        fields = ["name_of_event", "date_of_event"]

class JuriesforEvents(serializers.ModelSerializer):
    juries = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    first_name = serializers.ReadOnlyField(source='juries.first_name')
    last_name = serializers.ReadOnlyField(source='juries.last_name')
    patronymic = serializers.ReadOnlyField(source='juries.patronymic')
    job_title = serializers.ReadOnlyField(source='juries.job_title')
    class Meta():
        
        model = Events
        fields = "__all__"