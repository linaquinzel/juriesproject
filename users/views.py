from django.http import HttpRequest
from itertools import chain
from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Evaluation_Criterion, Events, Grades, Project, User
from .serializer import (
    Evaluation_CriterionSerializer, EventsSerializer, 
    ProjectSerializer, UserSerializer, VoteSerializer,
    RevoteSerializer, AddEventSerializer
)
from django.db.models.query import QuerySet


class UserViewSet(generics.RetrieveUpdateDestroyAPIView):
    """
    Список судей
    """
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = None
    
    

class EventsViewSet(generics.RetrieveUpdateDestroyAPIView):
    """
    Список мероприятий
    """
    permission_classes = [IsAdminUser]
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
        

class Evaluation_CriterionViewSet(generics.RetrieveUpdateDestroyAPIView):
    """
    Список критериев и оценок
    """
    permission_classes = [IsAdminUser]
    queryset = Evaluation_Criterion.objects.all()
    serializer_class = Evaluation_CriterionSerializer

class ProjectViewSet(generics.RetrieveUpdateDestroyAPIView):
    """
    Список проектов
    """
    permission_classes = [IsAdminUser]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class ReportViewSet(generics.ListAPIView):
    """
    Отчёт по мероприятию
    """
    permission_classes = [IsAdminUser]
    queryset = Evaluation_Criterion.objects.all().only("project", "evaluation_criterion", "grade")
    serializer_class = Evaluation_CriterionSerializer
    
class VoteViewSet(generics.RetrieveUpdateAPIView):
    """
    Голосование надо доделать флажок разрешения
    """
    permission_classes = [IsAuthenticated]
    queryset = Grades.objects.all()
    serializer_class = VoteSerializer

class RetrieveAPIView(mixins.RetrieveModelMixin,
                      generics.GenericAPIView):
    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        data = self.request.path
        return self.retrieve(request, *args, **kwargs)

class Revote(generics.DestroyAPIView):
    """
    Назначить переголосование надо доделать запрос ссылки
    """
    permission_classes = [IsAdminUser]
    queryset = Grades.objects.all().only("grade")
    serializer_class = RevoteSerializer
    

class EventLogViewSet(generics.ListAPIView):
    """
    Текущие мероприятия доделать фильтр по датам
    """
    permission_classes = [IsAuthenticated]
    queryset = Grades.objects.all().select_related("project")
    

class EventHistoryViewSet(generics.ListAPIView):
    """
    История мероприятий доделать фильтр по датам
    """
    permission_classes = [IsAuthenticated]
    queryset = Grades.objects.all().select_related("project")

class AddEventViewSet(generics.CreateAPIView):
    """
    Создать проект
    """
    permission_classes = [IsAdminUser]
    queryset = Events.objects.all().only("name_of_event", "date_of_event")
    serializer_class = AddEventSerializer

class AddUser(generics.CreateAPIView):
    """
    Добавить юзера
    """
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


    

