# models.py
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    no_of_travellers = Column(Integer, nullable=False)

    # Relationships
    travellers = relationship("Traveller", back_populates="trip")
    guide_id = Column(Integer, ForeignKey("guides.id"))
    guide = relationship("Guide", back_populates="trips")


class Traveller(Base):
    __tablename__ = "travellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    contact = Column(String)
    gender = Column(String)
    can_drive = Column(Boolean, default=False)
    smokes = Column(Boolean, default=False)
    drinks = Column(Boolean, default=False)
    on_medication = Column(Boolean, default=False)

    trip_id = Column(Integer, ForeignKey("trips.id"))
    trip = relationship("Trip", back_populates="travellers")


class Guide(Base):
    __tablename__ = "guides"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    operates_in = Column(String, nullable=False)
    languages = Column(String)  # can store as comma-separated for now
    can_drive = Column(Boolean, default=False)

    trips = relationship("Trip", back_populates="guide")
