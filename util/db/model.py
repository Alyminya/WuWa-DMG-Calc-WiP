
from typing import Literal

Weapon_Type = \
    Literal['sword'] |\
    Literal['broadblade'] |\
    Literal['pistols'] |\
    Literal['gauntlets'] |\
    Literal['rectifier']

Element = \
    Literal['spectro'] |\
    Literal['havoc'] |\
    Literal['glacio'] |\
    Literal['fusion'] |\
    Literal['aero'] |\
    Literal['electro']

Forte_Type = \
    Literal['a'] |\
    Literal['e'] |\
    Literal['f'] |\
    Literal['r'] |\
    Literal['i']

Move_Type = \
    Literal['a'] |\
    Literal['h'] |\
    Literal['p'] |\
    Literal['e'] |\
    Literal['r'] |\
    Literal['i'] |\
    Literal['o']

Substat = \
    Literal['atk'] |\
    Literal['hp'] |\
    Literal['def'] |\
    Literal['er'] |\
    Literal['cr'] |\
    Literal['cd']

class Move:
    id: str
    name: str
    forte_scaling: list[float]
    forte_type: Forte_Type
    stat_scaling: str
    move_type: Move_Type
    strikes: int
    after: list[str]|None
    chain: str|None
    sta_req: int|None
    fe_req: int|None
    fe_yield: int|None
    con_yield: int|None

class Character_Info:
    id: str
    name: str
    rarity: int
    weapon: Weapon_Type
    element: Element
    birthday: str|None
    affiliation: str|None
    birthplace: str|None
    base_hp_scaling: list[float]
    base_atk_scaling: list[float]
    base_def_scaling: list[float]
    max_fe: int
    moves: dict[str, Move]

class Weapon_Info:
    id: str
    name: str
    rarity: int
    type: Weapon_Type
    atk_scaling: list[float]
    sub_scaling: list[float]
    sub_stat: str

class DB:
    characters: dict[str, Character_Info]
    weapons: dict[str, Weapon_Info]