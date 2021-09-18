import graphene
from django.contrib.auth import get_user_model

from .schema import UserType


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=False)

    def mutate(self, info, **kwargs):
        instance = get_user_model().objects.create(**kwargs)
        instance.set_password(kwargs.get("password"))
        instance.save()
        return CreateUser(user=instance)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
