import graphene
from birinchi_topshiriq.models import Projects, Users, Task, Comments
from birinchi_topshiriq.role_permession import is_owner_maintainer, is_owner_developer
from birinchi_topshiriq.types_ import ProjectType,CommentType


class CreateProject(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        owner = graphene.List(graphene.Int, required=True)
        assignees = graphene.String()

    project = graphene.Field(ProjectType)

    @staticmethod
    @is_owner_maintainer
    def mutate(cls, info, name, description, owner, assignees):
        project = Projects(name=name, description=description, assignees=assignees)
        project.save()
        project.owner.set(Users.objects.filter(id__in=owner))

        return CreateProject(project=project)


class CreateComment(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
        task = graphene.Int(required=True)
        author = graphene.Int(required=True)

    comment = graphene.Field(CommentType)

    @staticmethod
    @is_owner_developer
    def mutate(cls, info, text, task, author):
        comment = Comments(text=text)
        comment.save()
        comment.task.set(Task.objects.filter(id=task))
        comment.author.set(Users.objects.filter(id=author))

        return CreateComment(comment=comment)





