from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NameAnalysisBase(BaseModel):
    name: str

class NameAnalysisCreate(NameAnalysisBase):
    pass

class NameAnalysisUpdate(BaseModel):
    name: Optional[str] = None
    analysis: Optional[str] = None
    personality_score: Optional[float] = None
    lucky_number: Optional[int] = None

class NameAnalysisResponse(NameAnalysisBase):
    id: int
    analysis: str
    personality_score: float
    lucky_number: int
    created_at: datetime
    
    class Config:
        from_attributes = True
