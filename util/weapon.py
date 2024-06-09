import json
import os.path
import math

from . import db

class Weapon:
    id: str
    name: str
    type: str
    level: int
    atk_scaling: list[float]
    sub_stat: str
    sub_scaling: list[float]

    def __init__(
        self,
        id: str,
        name: str,
        type: str,
        level: int,
        atk_scaling: list[float],
        sub_stat: str,
        sub_scaling: list[float]
    ):
        self.id = id
        self.name = name
        self.type = type
        self.level = level
        self.atk_scaling = atk_scaling
        self.sub_stat = sub_stat
        self.sub_scaling = sub_scaling
    
    @classmethod
    def by_id(cls, id: str, level: int):
        """Load character data from a CSV file."""
        weapon_info = db.data.weapons[id]
        return cls(
            id = id,
            name = weapon_info.name,
            level = level,
            type = str(weapon_info.type),
            atk_scaling = weapon_info.atk_scaling,
            sub_stat = weapon_info.sub_stat,
            sub_scaling = weapon_info.sub_scaling,
        )
    
    def ascension(self) -> int:
        asc = math.floor(self.level/10)
        if asc >= 3: asc -= 1
        if asc >= 1: asc -= 1
        return asc

    def base_atk(self) -> float:
        return self.atk_scaling[self.ascension()]

    def substat(self) -> tuple[str, float]:
        return self.sub_stat, self.sub_scaling[self.ascension()]

    def __str__(self):
        return (f"Weapon({self.name}, Type: {self.type}, Flat ATK: {self.base_atk()}, "
                f"ATK Bonus: {self.substat()[1]*100}%)")
