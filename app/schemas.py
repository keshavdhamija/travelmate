from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# ----------------------------
# Traveller Schemas
# ----------------------------
class TravellerBase(BaseModel):
    name: str
    age: int
    contact: str
    gender: Optional[str] = None
    can_drive: bool = False
    smokes: bool = False
    drinks: bool = False
    on_medication: bool = False


class TravellerCreate(TravellerBase):
    """Schema for creating a Traveller (input)."""
    pass


class TravellerResponse(TravellerBase):
    """Schema for returning a Traveller (output)."""
    id: int

    class Config:
        orm_mode = True


# ----------------------------
# Trip Schemas
# ----------------------------
class TripBase(BaseModel):
    origin: str
    destination: str
    start_date: date
    end_date: date
    no_of_travellers: int

class TravellerBase(BaseModel):
    name: str
    age: int
    contact: Optional[str] = None
    gender: Optional[str] = None
    can_drive: Optional[bool] = False
    smokes: Optional[bool] = False
    drinks: Optional[bool] = False
    on_medication: Optional[bool] = False

class TravellerCreate(TravellerBase):
    pass

class Traveller(TravellerBase):
    id: int

    class Config:
        orm_mode = True

class TripCreate(TripBase):
    """Schema for creating a Trip with Travellers."""
    travellers: List[TravellerCreate]


class TripResponse(TripBase):
    """Schema for returning a Trip with Travellers."""
    id: int
    travellers: List[TravellerResponse] = []

    class Config:
        orm_mode = True
