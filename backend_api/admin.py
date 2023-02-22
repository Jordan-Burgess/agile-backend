from django.contrib import admin
from .models import Profile, Project, User
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Project)
