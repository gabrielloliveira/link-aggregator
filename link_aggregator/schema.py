import graphene

from link_aggregator.core.mutations import Mutation as LinkMutation
from link_aggregator.core.schema import Query as LinkQuery
from link_aggregator.users.mutations import Mutation as UserMutation
from link_aggregator.users.schema import Query as UserQuery


class Query(LinkQuery, UserQuery, graphene.ObjectType):
    pass


class Mutation(LinkMutation, UserMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
