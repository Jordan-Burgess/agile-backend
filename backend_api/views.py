from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import ProfileSerializer
from .models import Profile

class Users(APIView):
    def get(self, request):
        data = Profile.objects.all()
        serializer = ProfileSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)