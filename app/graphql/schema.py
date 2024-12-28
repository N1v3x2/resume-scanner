import strawberry
from strawberry.file_uploads import Upload

from app.models.parsing import (
    School,
    Education,
    Experience,
    Experiences,
    Project,
    Projects,
    Leadership,
    ResearchRole,
    Research,
    Skills,
    ResumeInfo,
)
from app.models.scoring import (
    SectionScore,
    ReducedSectionScore,
    ResumeEvaluation,
    ResumeWeights,
    ScoredResume
)
from app.core.parsing.parsing import parse_resume
from app.core.scoring.scoring import score_resume

##### Parsing models #####
@strawberry.experimental.pydantic.type(model=School, all_fields=True)
class SchoolType:
    pass

@strawberry.experimental.pydantic.type(model=Education, all_fields=True)
class EducationType:
    pass

@strawberry.experimental.pydantic.type(model=Experience, all_fields=True)
class ExperienceType:
    pass

@strawberry.experimental.pydantic.type(model=Experiences, all_fields=True)
class ExperiencesType:
    pass

@strawberry.experimental.pydantic.type(model=Project, all_fields=True)
class ProjectType:
    pass

@strawberry.experimental.pydantic.type(model=Projects, all_fields=True)
class ProjectsType:
    pass

@strawberry.experimental.pydantic.type(model=Leadership, all_fields=True)
class LeadershipType:
    pass

@strawberry.experimental.pydantic.type(model=ResearchRole, all_fields=True)
class ResearchRoleType:
    pass

@strawberry.experimental.pydantic.type(model=Research, all_fields=True)
class ResearchType:
    pass

@strawberry.experimental.pydantic.type(model=Skills, all_fields=True)
class SkillsType:
    pass

@strawberry.experimental.pydantic.type(model=ResumeInfo, all_fields=True)
class ResumeInfoType:
    pass


##### Scoring models #####
@strawberry.experimental.pydantic.type(model=SectionScore, all_fields=True)
class SectionScoreType:
    pass

@strawberry.experimental.pydantic.type(model=ReducedSectionScore, all_fields=True)
class ReducedSectionScoreType:
    pass

@strawberry.experimental.pydantic.type(model=ResumeEvaluation, all_fields=True)
class ResumeEvaluationType:
    pass

@strawberry.experimental.pydantic.type(model=ResumeWeights, all_fields=True)
class ResumeWeightsType:
    pass

@strawberry.experimental.pydantic.type(model=ScoredResume, all_fields=True)
class ScoredResumeType:
    pass


@strawberry.type
class Query:
    @strawberry.field
    def hello_world(self) -> str:
        return "Hello World!"


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def parse_resume(self, resume: Upload) -> ResumeInfoType:
        resume_bytes = await resume.read()
        return ResumeInfoType.from_pydantic(parse_resume(resume_bytes))
    
    @strawberry.mutation
    async def score_resume(self, resume: Upload, job_desc: str) -> ScoredResumeType:
        resume_bytes = await resume.read()
        parsed_resume = parse_resume(resume_bytes)
        return ScoredResumeType.from_pydantic(score_resume(parsed_resume, job_desc))