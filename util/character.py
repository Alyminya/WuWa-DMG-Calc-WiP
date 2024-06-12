import math
from . import db

class Character:
    info: db.Character_Info
    level: int
    forte_levels: dict[db.Forte_Type, int]
    weapon: db.Weapon_Info

    def __init__(self, id: str, level: int, forte_levels: dict[db.Forte_Type, int]) -> None:
        self.info = db.data.characters[id]
        self.level = level
        self.forte_levels = forte_levels
        self.weapon = db.data.weapons["training-" + self.info.weapon]

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

    def stat(self, stat: db.Stat, after: str|None = None) -> float:
        base_value = 0.0
        match stat:
            case 'cr': base_value = 0.05
            case 'cd': base_value = 1.50
        bonus_value = 0.0
        for sn in self.info.res_chain:
            if sn.buff is None: continue
            buff = sn.buff
            if buff.target != "self": continue
            if buff.stat != stat: continue
            conditions_satisfied = True
            if buff.after is not None:
                for cond in buff.after:
                    if cond.move is not None and (after is None or cond.move != after):
                        conditions_satisfied = False
                        break
            if not conditions_satisfied:
                continue
            bonus_value += buff.amount
        total_value = base_value + bonus_value
        return total_value

    def em_bonus(self, after: str|None = None) -> float:
        em_bonus_stat: db.Stat
        match self.info.element:
            case 'glacio':  em_bonus_stat = 'glacio_dmg_bonus'
            case 'fusion':  em_bonus_stat = 'fusion_dmg_bonus'
            case 'electro': em_bonus_stat = 'electro_dmg_bonus'
            case 'aero':    em_bonus_stat = 'aero_dmg_bonus'
            case 'spectro': em_bonus_stat = 'spectro_dmg_bonus'
            case 'havoc':   em_bonus_stat = 'havoc_dmg_bonus'
        return self.stat(em_bonus_stat, after)

    def moves(self) -> dict[str, db.Move]:
        return self.info.moves
    
    def move_multiplier(self, move_id: str) -> float:
        move = self.info.moves[move_id]
        move_level = self.forte_levels[move.forte_type]
        multiplier = self.info.moves[move_id].forte_scaling[move_level-1]/100.0
        return multiplier

    def __str__(self) -> str:
        """String representation of the character."""
        return (f"Character({self.info.name}, Level: {self.level}, Base HP: {self.base_hp()}, "
                f"Base ATK: {self.base_atk()}, Base DEF: {self.base_def()}, Crit Rate: {self.stat('cr')*100}%, "
                f"Crit Damage: {self.stat('cd')*100}%)")
