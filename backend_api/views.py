from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import JsonResponse, HttpResponse
from .serializers import ProfileSerializer, ProjectSerializer, UserSerializer, RegisterSerializer
from .models import Profile, Project, User
from django.http import Http404
from rest_framework import status, generics

class Info(View):
    def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        return HttpResponse("Agile Backend")

class Users(APIView):
    def get(self, request):
        data = Profile.objects.all()
        serializer = ProfileSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ProfileInfo(APIView):
    def get_user_auth(self, id):
        return User.objects.all().filter(id=id)
    
    def get_user_profile(self, id):
        return Profile.objects.all().filter(user_id=id)

    def get(self, request, id):
        user = UserSerializer(self.get_user_auth(id), many=True)
        profile = ProfileSerializer(self.get_user_profile(id), many=True)
        return JsonResponse({"user": user.data, "profile": profile.data}, safe=False)

    def post(self, request, id):
        request.data['user'] = id
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors)

class Projects(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many =True)
        return JsonResponse(serializer.data, safe=False)


class ProjectDetails(APIView):
    def get_user_auth(self, id):
        return User.objects.all().filter(id=id)
    
    def get_user_profile(self, id):
        return Profile.objects.all().filter(user_id=id)

    def get_user_project(self, id):
        return Project.objects.all().filter(project_id=id)

    def get(self, request, id):
        user = UserSerializer(self.get_user_auth(id), many=True)
        profile = ProfileSerializer(self.get_user_profile(id), many=True)
        project = ProjectSerializer(self.get_user_project(id), many = True)
        return JsonResponse({"user": user.data, "profile": profile.data, "project": project.data}, safe=False)

    def post(self, request, id):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors)

    # def put(self, request, id, format=None):
    #     project = self.get_user_project(id)
    #     serializer = ProjectSerializer(project, data=request.data.get('project'))
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    # def delete(self, request, id, format=None):
    #     project = self.get_user_project(id)
    #     project.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)