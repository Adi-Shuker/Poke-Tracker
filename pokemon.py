from typing import List
from pydantic import BaseModel


class Pokemon(BaseModel):
    id: int
    name: str
    types: List
    height: int
    weight: int
    trainers: List
