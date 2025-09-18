from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from .. import models, database, schemas

router = APIRouter(
    prefix="/trips",
    tags=["Trips"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_trips(db: Session = Depends(get_db)):
    return db.query(models.Trip).all()

@router.post("/", response_model=schemas.TripResponse)
def create_trip(trip: schemas.TripCreate, db: Session = Depends(get_db)):
    # create object of Trip class
    db_trip = models.Trip(
        origin=trip.origin,
        destination=trip.destination,
        start_date=trip.start_date,
        end_date=trip.end_date,
        no_of_travellers=trip.no_of_travellers
    )
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)

    # add Travellers
    for traveller in trip.travellers:
        db_traveller = models.Traveller(
            name=traveller.name,
            age=traveller.age,
            contact=traveller.contact,
            gender=traveller.gender,
            can_drive=traveller.can_drive,
            smokes=traveller.smokes,
            drinks=traveller.drinks,
            on_medication=traveller.on_medication,
            trip_id=db_trip.id
        )
        db.add(db_traveller)

    db.commit()
    db.refresh(db_trip)

    return db_trip
