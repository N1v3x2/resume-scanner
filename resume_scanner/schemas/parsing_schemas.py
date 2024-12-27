from pydantic import BaseModel, RootModel

# Initial resume section parsing
class Resume(BaseModel):
    education: str
    experience: str
    projects: str
    leadership: str
    research: str
    skills: str
    
# Education
class School(BaseModel):
    name: str
    majors: list[str]
    minors: list[str]
    gpa: float = None
    grad_year: int
    honors: list[str]
    coursework: list[str]

class Education(BaseModel):
    data: list[School]

# Experience
class Experience(BaseModel):
    company: str
    role: str
    contributions: list[str]
    start_date: str
    end_date: str
    skills: list[str]
    
class Experiences(BaseModel):
    roles: list[Experience]
    yoe: float
    
# Projects
class Project(BaseModel):
    name: str
    contributions: list[str]
    skills: list[str]
    
class Projects(BaseModel):
    data: list[Project]

# Leadership
class Leadership(BaseModel):
    org: str
    role: str
    contributions: list[str]
    
# Research
class ResearchRole(BaseModel):
    institution: str
    role: str
    contributions: list[str]
    start_date: str
    end_date: str
    skills: list[str]
    
class Research(BaseModel):
    roles: list[ResearchRole]
    publications: list[str]

# Skills
class Skills(BaseModel):
    data: list[str]

# Final parsed resume info
class ResumeInfo(BaseModel):
    education: Education | None = None
    experience: Experiences | None = None
    projects: Projects | None = None
    leadership: Leadership | None = None
    research: Research | None = None
    skills: Skills | None = None