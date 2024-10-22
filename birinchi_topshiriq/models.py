# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
# # Create your models here.
#
# class TimeStampedModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True
#
# class Users(AbstractUser):
#     role=models.CharField(max_length=255,blank=True,null=True)
#
# class Projects(TimeStampedModel):
#     name=models.CharField(max_length=255,blank=True,null=True)
#     description=models.CharField(max_length=255,blank=True,null=True)
#     owner=models.ManyToManyField(Users,blank=True,null=True,related_name='projects')
#
#
# class Task(TimeStampedModel):
#     name=models.CharField(max_length=255,blank=True,null=True)
#     description=models.CharField(max_length=255,blank=True,null=True)
#     project=models.ForeignKey(Projects,blank=True,null=True,related_name='tasks')
#     status=models.CharField(max_length=255,blank=True,null=True)
#     deadline=models.DateField(blank=True,null=True)
#     assignees=models.CharField(max_length=255,blank=True,null=True)
#
#
# class Comments(TimeStampedModel):
#     text=models.CharField(max_length=255,blank=True,null=True)
#     task=models.ForeignKey(Task,blank=True,null=True,related_name='comments')
#     author=models.ForeignKey(Users,blank=True,null=True,related_name='comments')
#
# class Notifications(TimeStampedModel):
#     user=models.ForeignKey(Users,blank=True,null=True,related_name='notifications')
#     message=models.CharField(max_length=255,blank=True,null=True)
#     type=models.CharField(max_length=255,blank=True,null=True)
#     is_read=models.BooleanField(default=False)



