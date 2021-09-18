import graphene

from .models import Link


class CreateLink(graphene.Mutation):
    url = graphene.String()
    description = graphene.String()

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, **kwargs):
        Link.objects.create(**kwargs)
        return CreateLink(**kwargs)


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
