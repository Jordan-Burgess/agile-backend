from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.Users.as_view(), name="users"),
]