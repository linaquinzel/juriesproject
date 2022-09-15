from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(
        max_length=30,
        verbose_name="Имя",
        editable=True
    )
    last_name = models.CharField(
        max_length=30, 
        verbose_name="Фамилия", 
        editable=True
    )
    patronymic = models.CharField(
        max_length=30, 
        blank=True, 
        verbose_name="Отчество", 
        editable=True
    )
    job_title = models.CharField(
        max_length=300, 
        verbose_name="Должность", 
        editable=True
    )
    photo = models.ImageField(
        verbose_name="Фото профиля", 
        blank=True, 
        null=True
    )
    user_root = models.BooleanField(
        verbose_name="Админ ли?", 
        default=False, 
        editable=False,
        auto_created=True
    )
    
    
class Events(models.Model):
    name_of_event = models.CharField(
        max_length=300, 
        verbose_name="Название мероприятия", 
        editable=True
    )
    date_of_event = models.DateTimeField(
        verbose_name="Дата мероприятия",
        editable=True
    )

class Project(models.Model):
    event = models.ForeignKey(
        "Events",
        on_delete=models.CASCADE,
        verbose_name="Проекты"
    )
    name_of_project = models.CharField(
        max_length=300,
        verbose_name="Название проекта",
        editable=True,
    )
    speaker_name = models.CharField(
        max_length=150,
        verbose_name="Имя докладчика",
        editable=True
    )
    
    
class Grades(models.Model):
        
    author = models.ForeignKey(
        "User",
        verbose_name="Член жюри",
        on_delete=models.PROTECT
    )
        
    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        verbose_name="Оценённый проект"
    )
        
    grade = models.IntegerField(
        verbose_name="Оценка",
        editable=True,
        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]
    )
    evaluation_criterion = models.TextField(
        verbose_name="Критерий оценки",
        max_length=300,
        editable=True
    )
