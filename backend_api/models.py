from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.user.first_name
