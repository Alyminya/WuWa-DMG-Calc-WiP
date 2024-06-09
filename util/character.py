import json
import math
import os.path

from . import db

class Character:
    info: db.Character_Info
    level: int

    def __init__(self, id: str, level: int):
        self.info = db.data.characters[id]
        self.level = level

    def ascension(self) -> int:
        asc = math.floor(self.level / 10)
        if asc >= 3: asc -= 1 # Remove level 30 from ascensions
        if asc >= 1: asc -= 1 # Remove level 10 from ascensions
        return asc

    def base_hp(self) -> float:
        return self.info.base_hp_scaling[self.ascension()]

    def base_def(self) -> float:
        return self.info.base_def_scaling[self.ascension()]

    def base_atk(self) -> float:
        return self.info.base_atk_scaling[self.ascension()]

    def cr(self) -> float:
        return 0.05
    
    def cd(self) -> float:
        return 1.50

    def __str__(self):
        """String representation of the character."""
        return (f"Character({self.info.name}, Level: {self.level}, Base HP: {self.base_hp()}, "
                f"Base ATK: {self.base_atk()}, Base DEF: {self.base_def()}, Crit Rate: {self.cr()*100}%, "
                f"Crit Damage: {self.cd()*100}%)")
