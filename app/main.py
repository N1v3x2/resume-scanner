import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.extensions import AddValidationRules
from graphql.validation import NoSchemaIntrospectionCustomRule

from app.graphql.schema import Query, Mutation

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        AddValidationRules([NoSchemaIntrospectionCustomRule])
    ]
)

graphql_app = GraphQLRouter(schema, multipart_uploads_enabled=True, graphql_ide=None)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")