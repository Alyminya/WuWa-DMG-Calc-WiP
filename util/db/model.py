
from enum import Enum

Weapon_Type = Enum('Weapon_Type', ['sword', 'broadblade', 'pistols', 'gauntlets', 'rectifier'])

Element = Enum('Element', ['spectro', 'havoc', 'glacio', 'fusion', 'aero', 'electro'])

Substat = Enum('Substat', ['atk', 'hp', 'def', 'er', 'cr', 'cd'])

class Forte:
    id: str
    skill: str
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
    max_forte: int
    forte_multipliers: dict[str, list[float]]
    fortes: dict[str, Forte]


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