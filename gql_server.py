import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from resume_scanner.gql.schema import Query, Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema, multipart_uploads_enabled=True)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")