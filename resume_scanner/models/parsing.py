from pydantic import BaseModel
from typing import Optional

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
    gpa: Optional[float] = None
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
    
class LeadershipPositions(BaseModel):
    data: list[Leadership]
    
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
    education: Optional[list[School]]          = None
    experience: Optional[Experiences]       = None
    projects: Optional[list[Project]]       = None
    leadership: Optional[list[Leadership]]  = None
    research: Optional[Research]            = None
    skills: Optional[list[str]]             = None