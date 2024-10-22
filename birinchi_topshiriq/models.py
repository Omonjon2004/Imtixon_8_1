from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

User_Role=(
    ("Maintainer","Maintainer"),
    ("Developer",'Developer'),
    ("Notification",'Notification'),
)

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Users(AbstractUser):
    role=models.CharField(max_length=255,choices=User_Role,default="Notification")

class Projects(TimeStampedModel):
    name=models.CharField(max_length=255,blank=True,null=True)
    description=models.CharField(max_length=255,blank=True,null=True)
    owner=models.ManyToManyField(Users,related_name='projects')
    assignees = models.CharField(max_length=255, blank=True, null=True)


class Task(TimeStampedModel):
    name=models.CharField(max_length=255,blank=True,null=True)
    description=models.CharField(max_length=255,blank=True,null=True)
    project=models.ForeignKey(Projects,blank=True,null=True,related_name='tasks', on_delete=models.CASCADE)
    status=models.CharField(max_length=255,blank=True,null=True)
    deadline=models.DateField(blank=True,null=True)
    assignees=models.CharField(max_length=255,blank=True,null=True)


class Comments(TimeStampedModel):
    text=models.CharField(max_length=255,blank=True,null=True)
    task=models.ForeignKey(Task,blank=True,null=True,related_name='comments', on_delete=models.CASCADE)
    author=models.ForeignKey(Users,blank=True,null=True,related_name='comments',on_delete=models.CASCADE)

class Notifications(TimeStampedModel):
    user=models.ForeignKey(Users,blank=True,null=True,related_name='notifications', on_delete=models.CASCADE)
    message=models.CharField(max_length=255,blank=True,null=True)
    type=models.CharField(max_length=255,blank=True,null=True)
    is_read=models.BooleanField(default=False)



