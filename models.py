from pydantic import BaseModel
from typing import Optional


class Person(BaseModel):
    fName: str
    lName: str
    email: str
    phone: str
    age: int


class Car(BaseModel):
    brand: str
    model: str
    year: int
    color: Optional[str] = None
