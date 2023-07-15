from pydantic import BaseModel, condecimal, Field

from datetime import date
from typing import List


class Cargo(BaseModel):
    name: str
    cost: condecimal(decimal_places=2)
    cargo_type: str


# class CargoType(BaseModel):
#     cargo_type: str
#     rate: condecimal(decimal_places=4, max_digits=6)


# class Date(BaseModel):
#     date: date
#     options: List[CargoType]


class Tariff(BaseModel):
    json_: dict
