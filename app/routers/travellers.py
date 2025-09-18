from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database
from typing import List
router = APIRouter(
    prefix="/travellers",
    tags=["Travellers"]
)

# Dependency: DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------------
# GET all travellers
# -------------------------------
@router.get("/", response_model=List[schemas.Traveller])
def get_travellers(db: Session = Depends(get_db)):
    return db.query(models.Traveller).all()

# -------------------------------
# POST create a traveller
# -------------------------------
@router.post("/", response_model=schemas.Traveller)
def create_traveller(traveller: schemas.TravellerCreate, db: Session = Depends(get_db)):
    new_traveller = models.Traveller(**traveller.dict())
    db.add(new_traveller)
    db.commit()
    db.refresh(new_traveller)
    return new_traveller
