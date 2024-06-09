import json
import math
import os.path

from . import db

class Character:
    id: str
    name: str
    level: int
    hp_scaling: list[float]
    atk_scaling: list[float]
    defn_scaling: list[float]
    cr: float
    cd: float
    def __init__(
        self,
        id: str,
        name: str,
        level: int,
        hp_scaling: list[float],
        atk_scaling: list[float],
        defn_scaling: list[float]
    ):
        self.id = id
        self.name = name
        self.level = level
        self.hp_scaling = hp_scaling
        self.atk_scaling = atk_scaling
        self.defn_scaling = defn_scaling
        self.cr = 0.05
        self.cd = 1.50

    @classmethod
    def by_id(cls, id: str, level: int):
        """Load character data from a CSV file."""
        char_info = db.data.characters[id]
        return cls(
            id = id,
            name = char_info.name,
            level = level,
            hp_scaling = char_info.base_hp_scaling,
            atk_scaling = char_info.base_atk_scaling,
            defn_scaling = char_info.base_def_scaling,
        )

    def ascension(self) -> int:
        asc = math.floor(self.level / 10)
        if asc >= 3: asc -= 1 # Remove level 30 from ascensions
        if asc >= 1: asc -= 1 # Remove level 10 from ascensions
        return asc

    def base_hp(self) -> float:
        return self.hp_scaling[self.ascension()]

    def base_def(self) -> float:
        return self.defn_scaling[self.ascension()]

    def base_atk(self) -> float:
        return self.atk_scaling[self.ascension()]

    def __str__(self):
        """String representation of the character."""
        return (f"Character({self.name}, Level: {self.level}, Base HP: {self.base_hp()}, "
                f"Base ATK: {self.base_atk()}, Base DEF: {self.base_def()}, Crit Rate: {self.cr*100}%, "
                f"Crit Damage: {self.cd*100}%)")
