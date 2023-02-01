from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from .serializers import ProfileSerializer
from .models import Profile

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