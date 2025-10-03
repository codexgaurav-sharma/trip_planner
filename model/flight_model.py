from pydantic import BaseModel
from typing import Literal


class Flight(BaseModel):
    departure_airport_code: str
    arrival_airport_code: str
    departure_date: str
    cabin_class: Literal["Economy", "Business", "First"]
    number_of_adults: int
    number_of_children: int
    
    