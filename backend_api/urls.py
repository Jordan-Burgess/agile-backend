from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Info.as_view(), name="info"),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.Users.as_view(), name="users"),
]