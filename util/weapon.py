import math

from . import db

class Weapon:
    info: db.Weapon_Info
    level: int

    def __init__(self, id: str, level: int) -> type(self):
        self.info = db.data.weapons[id]
        self.level = level

    def ascension(self) -> int:
        asc = math.floor(self.level/10)
        if asc >= 3: asc -= 1
        if asc >= 1: asc -= 1
        return asc

    def base_atk(self) -> float:
        return self.info.atk_scaling[self.ascension()]

    def substat(self) -> tuple[str, float]:
        return self.info.sub_stat, self.info.sub_scaling[self.ascension()]

    def __str__(self) -> str:
        return (f"Weapon({self.info.name}, Type: {self.info.type}, Flat ATK: {self.base_atk()}, "
                f"ATK Bonus: {self.substat()[1]*100}%)")
