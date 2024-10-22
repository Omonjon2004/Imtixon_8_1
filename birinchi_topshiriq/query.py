import graphene
from graphene import ObjectType

from birinchi_topshiriq.models import Projects
from birinchi_topshiriq.types_ import ProjectType


class Query(ObjectType):
     projects=graphene.List(ProjectType)

     def resolve_projects(self, info):
         return Projects.objects.all()
