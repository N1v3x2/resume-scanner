from pydantic import BaseModel, Field

class MinReq(BaseModel):
    meets_req: bool = Field(..., alias="Meets Requirements")
    reasoning: str = Field(..., alias="Reasoning")
    
class Reasoning(BaseModel):
    skills: str     = Field(..., alias="Skills")
    experience: str = Field(..., alias="Experience")
    education: str  = Field(..., alias="Education")

class ResumeEvaluation(BaseModel):
    reasoning: Reasoning            = Field(..., alias="Reasoning")
    overall_assessment: str         = Field(..., alias="Overall Assessment")
    score: int                      = Field(..., alias="Score", ge=1, le=5)