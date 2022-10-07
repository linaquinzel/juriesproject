"""juriesproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import (
    UserViewSet, Evaluation_CriterionViewSet,
    ReportViewSet, EventsViewSet, VoteViewSet,
    EventLogViewSet, EventHistoryViewSet,
    JuriesforEventViewSet, ProjectViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('users/', UserViewSet.as_view({'get': 'list'})),
    path('users/<int:pk>/', UserViewSet.as_view({
        'get': 'retrieve',
        'post': 'create',
        'put': 'update',
        'delete': 'destroy',
        'patch': 'partial_update',
    })),
    path('grades/', Evaluation_CriterionViewSet.as_view({'get': 'list'})),
    path('grades/<int:pk>/', Evaluation_CriterionViewSet.as_view({
        'get': 'retrieve',
        'post': 'create',
        'put': 'update',
        'delete': 'destroy',
        'patch': 'partial_update',
    })),
    path('report/', ReportViewSet.as_view({'get': 'list'})),
    path('report/<int:pk>/', ReportViewSet.as_view({'get': 'retrieve'})),
    path('events/', EventsViewSet.as_view({'get': 'list'})),
    path('events/<int:pk>/', EventsViewSet.as_view({
        'get': 'retrieve',
        'post': 'create',
        'put': 'update',
        'delete': 'destroy',
        'patch': 'partial_update',
    })),
    path('vote/', VoteViewSet.as_view()),
    path('vote/<int:pk>/', VoteViewSet.as_view()),
    path('event_log/', EventLogViewSet.as_view({'get': 'list'})),
    path('event_history/', EventHistoryViewSet.as_view({'get': 'list'})),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('juriesforevent/<int:pk>/', JuriesforEventViewSet.as_view()),
    path('projects/<int:pk>/', ProjectViewSet.as_view()),
]
