import graphene

from link_aggregator.core.schema import Query as LinkQuery


class Query(LinkQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
