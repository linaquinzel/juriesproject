from django.utils import timezone
from django.db.models import Prefetch
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .models import Evaluation_Criterion, Events, Grades, Project, User
from .serializer import (
    AddEventSerializer, Evaluation_CriterionSerializer,
    EventsSerializer, ProjectSerializer, RevoteSerializer,
    UserSerializer, VoteSerializer, EventHistorySerializer,
    JuriesforEvents
)

class UserViewSet(viewsets.ModelViewSet):
    """
    Список судей
    """
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    

class EventsViewSet(viewsets.ModelViewSet):
    """
    Список мероприятий
    """
    permission_classes = [IsAdminUser]
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
        

class Evaluation_CriterionViewSet(viewsets.ModelViewSet):
    """
    Список критериев и оценок
    """
    permission_classes = [IsAdminUser]
    queryset = Evaluation_Criterion.objects.all()
    serializer_class = Evaluation_CriterionSerializer

class ProjectViewSet(generics.ListAPIView):
    """
    Список проектов
    """
    permission_classes = [IsAdminUser]
    serializer_class = ProjectSerializer
    def get_queryset(self):
        event_id = self.kwargs.get('pk')
        queryset = Project.objects.filter(event=event_id)
        return queryset
    
class ReportViewSet(viewsets.ModelViewSet):
    """
    Отчёт по мероприятию
    """
    permission_classes = [IsAdminUser]
    queryset = Grades.objects.all().only("project", "evaluation_criterion", "grade")
    serializer_class = Evaluation_CriterionSerializer
    
class VoteViewSet(generics.CreateAPIView, generics.RetrieveUpdateAPIView):
    """
    Голосование
    """
    permission_classes = [IsAuthenticated]
    serializer_class = VoteSerializer

    def get_queryset(self):
        task_id = self.kwargs.get('pk')
        fltr = Project.objects.get(pk=task_id)
        flag = fltr.start_project
        if flag:
            queryset = Grades.objects.filter(project=task_id)
            return queryset

    def perform_create(self, serializer):
        task_id = self.kwargs.get('pk')
        fltr = Project.objects.get(pk=task_id)
        flag = fltr.start_project
        if flag:
            serializer.save()
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class Revote(generics.DestroyAPIView):
    """
    Назначить переголосование
    """
    permission_classes = [IsAdminUser]
    queryset = Grades.objects.all().only("grade")
    serializer_class = RevoteSerializer
    

class EventLogViewSet(viewsets.ModelViewSet):
    """
    Текущие мероприятия
    """
    date = str(timezone.now())
    dt = date.split(" ")
    permission_classes = [IsAuthenticated]
    serializer_class = EventsSerializer
    queryset = Events.objects.filter(date_of_event__startswith=(dt[0]))
    

class EventHistoryViewSet(viewsets.ModelViewSet):
    """
    История мероприятий
    """
    date = str(timezone.now())
    dt = date.split(" ")
    permission_classes = [IsAuthenticated]
    serializer_class = EventHistorySerializer
    queryset = Grades.objects.filter(event__date_of_event__lte=dt[0]).select_related("project").select_related("event").all()

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

class JuriesforEventViewSet(generics.RetrieveUpdateAPIView):
    """
    Список судей в мероприятии
    """
    permission_classes = [IsAdminUser]
    queryset = Events.objects.select_related("juries").all()
    serializer_class = JuriesforEvents
    

