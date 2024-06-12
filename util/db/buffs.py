
from typing import Literal, Any

from util.db.model import Scaling_Substat

Bonus_Substat = \
    Literal['atk_prc'] |\
    Literal['hp_prc'] |\
    Literal['def_prc'] |\
    Literal['er'] |\
    Literal['cr'] |\
    Literal['cd'] |\
    Literal['a_dmg'] |\
    Literal['h_dmg'] |\
    Literal['e_dmg'] |\
    Literal['r_dmg'] |\
    Literal['spectro_dmg'] |\
    Literal['havoc_dmg'] |\
    Literal['glacio_dmg'] |\
    Literal['electro_dmg'] |\
    Literal['fusion_dmg'] |\
    Literal['aero_dmg'] |\
    Literal['atk_flat'] |\
    Literal['def_flat'] |\
    Literal['hp_flat']

Recoverable_Substat = \
    Literal['hp']  |\
    Literal['sta'] |\
    Literal['fe']  |\
    Literal['ce']

Debuff_Substat = \
    Literal['spectro_res'] |\
    Literal['havoc_res'] |\
    Literal['glacio_res'] |\
    Literal['electro_res'] |\
    Literal['fusion_res'] |\
    Literal['aero_res']

Condition_Kind = \
    Literal['stat_less'] |\
    Literal['stat_greater']

class Condition:
    kind: Condition_Kind
    stat: Scaling_Substat
    amount: float

Buff_Kind = \
    Literal['stat_boost'] |\
    Literal['stat_recovery'] |\
    Literal['attack_dmg_boost']

class Buff:
    kind: Buff_Kind
    events_id: list[str]|None
    timeout_sec: float|None
    condition: Condition|None
    def __init__(self, kind: Buff_Kind, timeout_sec: float|None, events_id: list[str]|None, condition: Condition|None) -> None:
        self.kind = kind
        self.timeout_sec = timeout_sec
        self.events_id = events_id
        self.condition = condition

class Stat_Boost(Buff):
    stat: Bonus_Substat
    amount: float
    def __init__(self, stat: Bonus_Substat, amount: float, *args, **kwargs) -> None:
        super().__init__('stat_boost', *args, **kwargs)
        self.stat = stat
        self.amount = amount

class Stat_Recovery(Buff):
    stat: Recoverable_Substat
    amount: float
    scale_of: Scaling_Substat|None
    def __init__(self, stat: Recoverable_Substat, amount: float, scale_of: Scaling_Substat, *args, **kwargs) -> None:
        super().__init__('stat_recovery', *args, **kwargs)
        self.stat = stat
        self.amount = amount
        self.scale_of = scale_of

class Debuff(Buff):
    stat: Debuff_Substat
    amount: float
    def __init__(self, stat: Debuff_Substat, amount: float, *args, **kwargs) -> None:
        super().__init__('stat_recovery', *args, **kwargs)
        self.stat = stat
        self.amount = amount

class Attack_DMG_Boost(Buff):
    attack_id: str
    amount: float
    def __init__(self, attack_id: str, amount: float, *args, **kwargs) -> None:
        super().__init__('attack_dmg_boost', *args, **kwargs)
        self.attack_id = attack_id
        self.amount = amount

