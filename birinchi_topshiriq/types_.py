from graphene_django import DjangoObjectType

from birinchi_topshiriq.models import Projects, Task, Comments


class ProjectType(DjangoObjectType):
    class Meta:
        model=Projects
        fields=["id","name","description","owner","assignees"]


class TaskType(DjangoObjectType):
    class Meta:
        model=Task
        fields=["id","name","description","project","status","assignees","deadline"]


class CommentType(DjangoObjectType):
    class Meta:
        model=Comments
        fields=["id","text","task","author"]
