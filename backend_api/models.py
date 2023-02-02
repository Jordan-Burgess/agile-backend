from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.user.first_name
        
class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    TOPIC_CHOICES = [
        ('ART', 'Art'),
        ('CAR', 'Career'),
        ('COM', 'Community'),
        ('CUL', 'Culture'),
        ('ECO','Environmental'),
        ('EDU', 'Education'),
        ('FNC','Finance'),
        ('FOD', 'Food'),
        ('MED', 'Media/Pop Culture'),
        ('MD', 'Medical'),
        ('REL', 'Religion'),
        ('SOC', 'Social'),
        ('SJ','Social Justice'),
        ('SPT', 'Sports'),
        ('IT', 'Technology'),
        ('TRV', 'Travel'),
    ]
    title = models.CharField(max_length=50)
    topic = models.CharField(max_length=3,choices=TOPIC_CHOICES)
    

    