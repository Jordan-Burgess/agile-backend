from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Info.as_view(), name="info"),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.Users.as_view(), name="users"),
    path('users/<int:id>', views.ProfileInfo.as_view(), name="users"),
    path('projects/', views.Projects.as_view(), name="projects" ),
    path('projects/<int:pk>',views.ProjectDetail.as_view()),
]