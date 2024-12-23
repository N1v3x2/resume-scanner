from pydantic import BaseModel, RootModel, Field

class Resume(BaseModel):
    experience: str = Field(..., alias="Experience")
    education: str  = Field(..., alias="Education")
    skills: str     = Field(..., alias="Skills")
    projects: str   = Field(..., alias="Projects")
    leadership: str = Field(..., alias="Leadership")
    research: str   = Field(..., alias="Research")
    
class School(BaseModel):
    name: str           = Field(..., alias="Name")
    majors: list[str]   = Field(..., alias="Majors")
    minors: list[str]   = Field(..., alias="Minors")
    gpa: float          = Field(None, alias="GPA")
    grad_year: int      = Field(..., alias="Graduation Year")

class Education(RootModel[list[School]]):
    pass

class Experience(BaseModel):
    company: str = Field(..., alias="Company")
    role: str = Field(..., alias="Role")
    contributions: list[str] = Field(..., alias="Contributions")
    
class Experiences(BaseModel):
    experiences: list[Experience] = Field(..., alias="Experiences")
    yoe: float = Field(..., alias="Total Years of Experience")
    
class Skills(BaseModel):
    technical_skills: list[str] = Field(..., alias="Technical Skills")
    domain_specific_skills: list[str] = Field(..., alias="Domain-Specific Skills")