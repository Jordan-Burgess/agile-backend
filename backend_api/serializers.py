from rest_framework import serializers
from .models import Profile, Project, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__' 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'