import graphene
from birinchi_topshiriq.mutations import CreateProject, CreateComment
from birinchi_topshiriq.query import Query


class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    create_comment = CreateComment.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)

__all__ =("schema",)