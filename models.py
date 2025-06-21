from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func


Base = declarative_base()

class NameAnalysis(Base):
    __tablename__ = "name_analyses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    analysis = Column(String(500))
    personality_score = Column(Float)
    lucky_number = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
