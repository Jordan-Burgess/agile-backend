from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES= [
        ('FS', 'FullStack'),
        ('FE', 'FrontEnd'),
        ('BE', 'BackEnd'),
        ('UX', 'UX/UI Designer')
    ]
    photo = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    bio = models.TextField()
    twitter_link = models.CharField(max_length=200)
    github_link = models.CharField(max_length=200)
    linkedin_link = models.CharField(max_length=200)
    portfolio_link = models.CharField(max_length=200) 
    figma_link = models.CharField(max_length=200) 
    jira_link = models.CharField(max_length=200) 
    trello_link = models.CharField(max_length=200) 
    slack_link = models.CharField(max_length=200) 
    google_drive_link = models.CharField(max_length=200) 
    microsoft_teams_links = models.CharField(max_length=200) 
    zoom_link = models.CharField(max_length=200) 
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)
    tools = models.TextField()
    bootcamp_grad = models.BooleanField(default= False)
    self_taught = models.BooleanField(default = False)
    cs_degree = models.BooleanField(default = False)
    industry_prof = models.BooleanField(default = False)

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
    technology = models.TextField()
    roles = models.TextField()


    