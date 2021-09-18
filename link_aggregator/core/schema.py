import django_filters
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Link


class LinkFilter(django_filters.FilterSet):
    class Meta:
        model = Link
        fields = ["url", "description"]


class LinkNode(DjangoObjectType):
    class Meta:
        model = Link
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    link = graphene.relay.Node.Field(LinkNode)
    links = DjangoFilterConnectionField(LinkNode, filterset_class=LinkFilter)
