import strawberry
import redis
from fastapi import FastAPI, Depends
from strawberry.fastapi import GraphQLRouter
from strawberry.extensions import AddValidationRules
from graphql.validation import NoSchemaIntrospectionCustomRule

from app.graphql.schema import Query, Mutation

pool = redis.ConnectionPool(host="localhost", port=6379, db=0, max_connections=10)

def get_redis_client():
    return redis.Redis(connection_pool=pool)

def get_context(redis_client=Depends(get_redis_client)):
    return {"redis_client": redis_client}

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        AddValidationRules([NoSchemaIntrospectionCustomRule])
    ]
)

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
    multipart_uploads_enabled=True,
    graphql_ide=None
)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")