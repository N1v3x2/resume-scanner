from pydantic import BaseModel, Field
    
class SectionScore(BaseModel):
    relevance: int  = Field(..., description="Relevance score (0-5)")
    depth: int      = Field(..., description="Depth score (0-5)")
    impact: int     = Field(..., description="Impact score (0-5)")
    comment: str    = Field(..., description="Explanation for the scores in this section")
    
class ReducedSectionScore(BaseModel):
    alignment: int  = Field(..., description="Alignment score (0-5)")
    comment: str    = Field(..., description="Explanation for the score in this section")

class ResumeEvaluation(BaseModel):
    experience: SectionScore         
    education: ReducedSectionScore   
    projects: SectionScore           
    leadership: SectionScore         
    research: SectionScore           
    skills: ReducedSectionScore      
    overall_comment: str = Field(..., description="General comments about the resume, including strengths and weaknesses")
    
class ResumeWeights(BaseModel):
    reasoning: str
    validation: str
    education: float
    experience: float
    projects: float
    leadership: float
    research: float
    skills: float

class ScoredResume(BaseModel):
    resume_eval: ResumeEvaluation
    resume_weights: ResumeWeights
    final_score: float