from pydantic import BaseModel, Field

class MinReq(BaseModel):
    meets_req: bool = Field(..., alias="Meets Requirements")
    reasoning: str = Field(..., alias="Reasoning")
    
class ResumeScore(BaseModel):
    score: int                  = Field(..., alias="Score", ge=0, le=10)
    justification: list[str]    = Field(..., alias="Justification")