
from typing import Union, Literal

Weapon_Type = Union[
    Literal['sword'],
    Literal['broadblade'],
    Literal['pistols'],
    Literal['gauntlets'],
    Literal['rectifier'],
]

Element = Union[
    Literal['spectro'],
    Literal['havoc'],
    Literal['glacio'],
    Literal['fusion'],
    Literal['aero'],
    Literal['electro'],
]

Forte_Type = Union[
    Literal['a'],
    Literal['e'],
    Literal['f'],
    Literal['r'],
    Literal['i'],
]

Move_Type = Union[
    Literal['a'],
    Literal['h'],
    Literal['p'],
    Literal['e'],
    Literal['r'],
    Literal['i'],
    Literal['o'],
]

Substat = Union[
    Literal['atk'],
    Literal['hp'],
    Literal['def'],
    Literal['er'],
    Literal['cr'],
    Literal['cd'],
]

Stat = Union[
    Literal['hp'],
    Literal['atk'],
    Literal['def'],
    Literal['sta'], # Stamina
    Literal['cr'], # Crit rate
    Literal['cd'], # Crit damage
    Literal['er'], # Energy regeneration
    Literal['e_dmg_bonus'],
    Literal['a_dmg_bonus'],
    Literal['h_dmg_bonus'],
    Literal['r_dmg_bonus'],
    Literal['physical_dmg_bonus'],
    Literal['glacio_dmg_bonus'],
    Literal['fusion_dmg_bonus'],
    Literal['electro_dmg_bonus'],
    Literal['aero_dmg_bonus'],
    Literal['spectro_dmg_bonus'],
    Literal['havoc_dmg_bonus'],
    Literal['physical_dmg_res'],
    Literal['glacio_dmg_res'],
    Literal['fusion_dmg_res'],
    Literal['electro_dmg_res'],
    Literal['aero_dmg_res'],
    Literal['spectro_dmg_res'],
    Literal['havoc_dmg_res'],
    Literal['hb'] # Healing Bonus
]

class Buff_Condition:
    move: None|str

class Buff:
    id: str
    stat: Stat
    amount: float
    target: Literal['self']|Literal['enemy']
    after: None|list[Buff_Condition]

class Sequence_Node:
    name: str
    buff: None|Buff

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
    res_chain: list[Sequence_Node]

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