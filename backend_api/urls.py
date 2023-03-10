from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Info.as_view(), name="info"),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.Users.as_view(), name="users"),
    path('users/<str:id>', views.ProfileInfo.as_view(), name="users"),
    path('register/<str:id>', views.RegisterView.as_view(), name="users"),
    path('projects/', views.Projects.as_view(), name="projects" ),
    path('projects/<int:pk>',views.ProjectDetails.as_view()),
]