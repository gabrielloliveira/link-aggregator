import graphene

from link_aggregator.core.mutations import Mutation as LinkMutation
from link_aggregator.core.schema import Query as LinkQuery


class Query(LinkQuery, graphene.ObjectType):
    pass


class Mutation(LinkMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
