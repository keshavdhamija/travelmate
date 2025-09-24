# schemas.py
from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class TravellerBase(BaseModel):
    name: str
    age: int
    contact: Optional[str] = None
    gender: Optional[str] = None
    can_drive: bool = False
    smokes: bool = False
    drinks: bool = False
    on_medication: bool = False

class Traveller(TravellerBase):
    id: int
    class Config:
        orm_mode = True


class GuideBase(BaseModel):
    name: str
    age: int
    operates_in: str
    languages: List[str]
    can_drive: bool = False

class Guide(GuideBase):
    id: int
    class Config:
        orm_mode = True


class TripBase(BaseModel):
    origin: str
    destination: str
    start_date: date
    end_date: date
    no_of_travellers: int

class TripCreate(TripBase):
    pass

class Trip(TripBase):
    id: int
    travellers: List[Traveller] = []
    guide: Optional[Guide] = None

    class Config:
        orm_mode = True
