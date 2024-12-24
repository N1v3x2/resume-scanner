from pydantic import BaseModel, RootModel, Field

# Job Description
class JobDescription(BaseModel):
    required_skills: list[str]          = Field(..., alias="Required Skills")
    preferred_skills: list[str]         = Field(..., alias="Preferred Skills")
    required_experience: list[str]      = Field(..., alias="Required Experience")
    preferred_experience: list[str]     = Field(..., alias="Preferred Experience")
    required_education: list[str]       = Field(..., alias="Required Education")
    preferred_education: list[str]      = Field(..., alias="Preferred Education")

# Initial resume section parsing
class Resume(BaseModel):
    education: str  = Field(..., alias="Education")
    experience: str = Field(..., alias="Experience")
    projects: str   = Field(..., alias="Projects")
    leadership: str = Field(..., alias="Leadership")
    research: str   = Field(..., alias="Research")
    skills: str     = Field(..., alias="Skills")
    
# Education
class School(BaseModel):
    name: str               = Field(..., alias="Name")
    majors: list[str]       = Field(..., alias="Majors")
    minors: list[str]       = Field(..., alias="Minors")
    gpa: float              = Field(None, alias="GPA")
    grad_year: int          = Field(..., alias="Graduation Year")
    honors: list[str]       = Field(..., alias="Honors")
    coursework: list[str]   = Field(..., alias="Coursework")

class Education(RootModel[list[School]]):
    pass

# Experience
class Experience(BaseModel):
    company: str                = Field(..., alias="Company")
    role: str                   = Field(..., alias="Role")
    contributions: list[str]    = Field(..., alias="Contributions")
    start_date: str             = Field(..., alias="Start Date")
    end_date: str               = Field(..., alias="End Date")
    skills: list[str]           = Field(..., alias="Skills")
    
class Experiences(BaseModel):
    roles: list[Experience] = Field(..., alias="Roles")
    yoe: float              = Field(..., alias="YOE")
    
# Projects
class Project(BaseModel):
    name: str                   = Field(..., alias="Name")
    contributions: list[str]    = Field(..., alias="Contributions")
    skills: list[str]           = Field(..., alias="Skills")
    
class Projects(RootModel[list[Project]]):
    pass

# Leadership
class Leadership(BaseModel):
    org: str                    = Field(..., alias="Organization")
    role: str                   = Field(..., alias="Role")
    contributions: list[str]    = Field(..., alias="Contributions")
    
# Research
class ResearchRole(BaseModel):
    institution: str            = Field(..., alias="Institution")
    role: str                   = Field(..., alias="Role")
    contributions: list[str]    = Field(..., alias="Contributions")
    start_date: str             = Field(..., alias="Start Date")
    end_date: str               = Field(..., alias="End Date")
    skills: list[str]           = Field(..., alias="Skills")
    
class Research(BaseModel):
    roles: list[ResearchRole]   = Field(..., alias="Roles")
    publications: list[str]     = Field(..., alias="Publications")

# Skills
class Skills(RootModel[list[str]]):
    pass