import strawberry

from resume_scanner.gql.schema import Query, Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)