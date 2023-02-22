from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    pass

    password = models.CharField(max_length=50, blank=False, null=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
    ROLE_CHOICES = [
        ('FS', 'FullStack'),
        ('FE', 'FrontEnd'),
        ('BE', 'BackEnd'),
        ('UX', 'UX/UI Designer'),
        ('PM', 'Project Manager')
    ]
    photo = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    bio = models.TextField()
    twitter_link = models.CharField(max_length=200)
    github_link = models.CharField(max_length=200)
    linkedin_link = models.CharField(max_length=200)
    portfolio_link = models.CharField(max_length=200)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)
    tools = models.TextField()
    bootcamp_grad = models.BooleanField(default=False)
    self_taught = models.BooleanField(default=False)
    cs_degree = models.BooleanField(default=False)
    industry_prof = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name


class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False)
    TOPIC_CHOICES = [
        ('ART', 'Art'),
        ('CAR', 'Career'),
        ('COM', 'Community'),
        ('CUL', 'Culture'),
        ('ECO', 'Environmental'),
        ('EDU', 'Education'),
        ('FNC', 'Finance'),
        ('FOD', 'Food'),
        ('MED', 'Media/Pop Culture'),
        ('MD', 'Medical'),
        ('REL', 'Religion'),
        ('SOC', 'Social'),
        ('SJ', 'Social Justice'),
        ('SPT', 'Sports'),
        ('IT', 'Technology'),
        ('TRV', 'Travel'),
    ]
    ROLE_CHOICES = [
        ('FS', 'FullStack'),
        ('FE', 'FrontEnd'),
        ('BE', 'BackEnd'),
        ('UX', 'UX/UI Designer'),
        ('PM', 'Project Manager')
    ]
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    project_members = models.ManyToManyField(
        User, blank=False)  # Must at least receive the creating user as a member
    tech = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    roles = ArrayField(models.CharField(
        max_length=2, choices=ROLE_CHOICES), blank=True, null=True)
    figma_link = models.CharField(max_length=200, blank=True)
    jira_link = models.CharField(max_length=200, blank=True)
    trello_link = models.CharField(max_length=200, blank=True)
    slack_link = models.CharField(max_length=200, blank=True)
    google_drive_link = models.CharField(max_length=200, blank=True)
    microsoft_teams_link = models.CharField(max_length=200, blank=True)
    zoom_link = models.CharField(max_length=200, blank=True)
    github_frontend_link = models.CharField(max_length=200, blank=True)
    github_backend_link = models.CharField(max_length=200, blank=True)
    topics = ArrayField(models.CharField(
        max_length=3, choices=TOPIC_CHOICES), blank=True, null=True)

    def __str__(self):
        return self.title
