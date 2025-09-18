from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    no_of_travellers = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    # Relationship with Traveller
    travellers = relationship("Traveller", back_populates="trip", cascade="all, delete-orphan")


class Traveller(Base):
    __tablename__ = "travellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    contact = Column(String, nullable=False)
    gender = Column(String, nullable=False)  # could be "M/F/Other"
    can_drive = Column(Boolean, default=False)
    smokes = Column(Boolean, default=True)
    drinks = Column(Boolean, default=True)
    on_medication = Column(Boolean, default=True)

    # Foreign key to Trip
    trip_id = Column(Integer, ForeignKey("trips.id"))

    # Relationship back to Trip
    trip = relationship("Trip", back_populates="travellers")
