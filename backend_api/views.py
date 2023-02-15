from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from .serializers import ProfileSerializer, ProjectSerializer, UserSerializer
from .models import Profile, Project, User

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
        data = Project.objects.all()
        serializer = ProjectSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)