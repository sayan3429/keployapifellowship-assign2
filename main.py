from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List
import random
import hashlib

from database import engine, get_db
from models import Base, NameAnalysis
from schemas import NameAnalysisCreate, NameAnalysisResponse, NameAnalysisUpdate


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Name Analyzer API", version="1.0.0")

app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.get("/")
async def root():
    return {"message": "Welcome to the Name Analyzer API!"}


ANALYSES = [
    "Your name radiates positive energy and charisma!",
    "People with your name are natural-born leaders.",
    "Your name suggests creativity and artistic talent.",
    "You have a name that inspires trust and reliability.",
    "Your name is associated with intelligence and wisdom.",
    "People with your name tend to be adventurous spirits.",
    "Your name has a mysterious and intriguing quality.",
    "You possess a name that suggests kindness and empathy.",
    "Your name indicates strong communication skills.",
    "People with your name are known for their determination."
]

def generate_analysis(name: str):
    """Generate analysis based on name"""
    name_hash = hashlib.md5(name.lower().encode()).hexdigest()
    analysis_index = int(name_hash[:2], 16) % len(ANALYSES)
    analysis = ANALYSES[analysis_index]
    personality_score = round((int(name_hash[2:4], 16) / 255) * 10, 1)
    lucky_number = (int(name_hash[4:6], 16) % 100) + 1
    return analysis, personality_score, lucky_number


@app.post("/analyze", response_model=NameAnalysisResponse)
def create_name_analysis(name_data: NameAnalysisCreate, db: Session = Depends(get_db)):
    """Analyze a name and store the result"""
    existing = db.query(NameAnalysis).filter(NameAnalysis.name == name_data.name.lower()).first()
    if existing:
        raise HTTPException(status_code=400, detail="Name already analyzed")
    analysis, personality_score, lucky_number = generate_analysis(name_data.name)
    db_analysis = NameAnalysis(
        name=name_data.name.lower(),
        analysis=analysis,
        personality_score=personality_score,
        lucky_number=lucky_number
    )
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis


@app.get("/analyses", response_model=List[NameAnalysisResponse])
def get_all_analyses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all name analyses with pagination"""
    analyses = db.query(NameAnalysis).offset(skip).limit(limit).all()
    return analyses


@app.get("/analyses/{analysis_id}", response_model=NameAnalysisResponse)
def get_analysis(analysis_id: int, db: Session = Depends(get_db)):
    """Get a specific name analysis by ID"""
    analysis = db.query(NameAnalysis).filter(NameAnalysis.id == analysis_id).first()
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return analysis

@app.put("/analyses/{analysis_id}", response_model=NameAnalysisResponse)
def update_analysis(analysis_id: int, update_data: NameAnalysisUpdate, db: Session = Depends(get_db)):
    """Update an existing name analysis"""
    db_analysis = db.query(NameAnalysis).filter(NameAnalysis.id == analysis_id).first()
    if not db_analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    if update_data.name:
        db_analysis.name = update_data.name.lower()
    if update_data.analysis:
        db_analysis.analysis = update_data.analysis
    if update_data.personality_score is not None:
        db_analysis.personality_score = update_data.personality_score
    if update_data.lucky_number is not None:
        db_analysis.lucky_number = update_data.lucky_number
    db.commit()
    db.refresh(db_analysis)
    return db_analysis


@app.delete("/analyses/{analysis_id}")
def delete_analysis(analysis_id: int, db: Session = Depends(get_db)):
    """Delete a name analysis"""
    db_analysis = db.query(NameAnalysis).filter(NameAnalysis.id == analysis_id).first()
    if not db_analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    db.delete(db_analysis)
    db.commit()
    return {"message": "Analysis deleted successfully"}


@app.get("/analyze/{name}", response_model=NameAnalysisResponse)
def get_analysis_by_name(name: str, db: Session = Depends(get_db)):
    """Get analysis for a specific name"""
    analysis = db.query(NameAnalysis).filter(NameAnalysis.name == name.lower()).first()
    if not analysis:
        raise HTTPException(status_code=404, detail="Name not found. Analyze it first!")
    return analysis
