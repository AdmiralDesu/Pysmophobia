import datetime
from pydantic import BaseModel
from typing import Union, List, Dict


class Cards(BaseModel):
    game_id: Union[int, str, None]
    cards: List[str]


class Player(BaseModel):
    player_id: Union[int, str, None]
    name: str


class Game(BaseModel):
    game_id: Union[int, str, None]
    game_version: str
    duration: datetime.time
    ghost_id: int
    difficulty: str
    evidences: List[int]
    players: List[int]
    players_results: Dict[str, int]
    dead_players: Dict[str, int]
    cursed_possession: str
    tasks: List[str]


class Ghost(BaseModel):
    ghost_id: Union[int, str, None]
    name: str
    evidences: Dict[str, str]
    strength: Union[List[str], None]
    weakness: Union[List[str], None]
    ability: Union[List[str], None]
    uniqueness: Union[List[str], None]


