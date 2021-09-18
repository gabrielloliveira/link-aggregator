import graphene
from django.contrib.auth import get_user_model
from django.db.models import Q
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    users = graphene.List(UserType, q=graphene.String())

    @login_required
    def resolve_users(self, info, **kwargs):
        qs = get_user_model().objects.all()
        if kwargs.get("q"):
            q = kwargs.get("q")
            qs = qs.filter(
                Q(username__icontains=q)
                | Q(first_name__icontains=q)
                | Q(email__icontains=q)
            )
        return qs
