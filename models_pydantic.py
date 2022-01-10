import datetime
from pydantic import BaseModel


class Player(BaseModel):
    name: str


class Game(BaseModel):
    duration: datetime.time
    ghost_id: int
    difficulty: str
    evidences: list
    players: list
    right_or_not: list
    dead_or_not: list


class Ghost(BaseModel):
    name: str
    evidences: dict
    strength: str
    weakness: str


