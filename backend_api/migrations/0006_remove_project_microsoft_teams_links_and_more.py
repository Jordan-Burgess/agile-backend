# Generated by Django 4.1.2 on 2023-02-22 19:58

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend_api', '0005_project_github_backend_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='microsoft_teams_links',
        ),
        migrations.RemoveField(
            model_name='project',
            name='topic',
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='microsoft_teams_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='project_members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='roles',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('FS', 'FullStack'), ('FE', 'FrontEnd'), ('BE', 'BackEnd'), ('UX', 'UX/UI Designer'), ('PM', 'Project Manager')], max_length=2), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='project',
            name='tech',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='project',
            name='topics',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('ART', 'Art'), ('CAR', 'Career'), ('COM', 'Community'), ('CUL', 'Culture'), ('ECO', 'Environmental'), ('EDU', 'Education'), ('FNC', 'Finance'), ('FOD', 'Food'), ('MED', 'Media/Pop Culture'), ('MD', 'Medical'), ('REL', 'Religion'), ('SOC', 'Social'), ('SJ', 'Social Justice'), ('SPT', 'Sports'), ('IT', 'Technology'), ('TRV', 'Travel')], max_length=3), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('FS', 'FullStack'), ('FE', 'FrontEnd'), ('BE', 'BackEnd'), ('UX', 'UX/UI Designer'), ('PM', 'Project Manager')], max_length=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='figma_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_backend_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_frontend_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='google_drive_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='jira_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='slack_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='trello_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='zoom_link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
