import sympy as sp

from .character import Character
from .weapon import Weapon

# def define_damage_formula():
#     CharacterATK, WeaponATK, bonusATK_percent, bonus_flat_ATK = sp.symbols('CharacterATK WeaponATK bonusATK_percent bonus_flat_ATK')
#     SkillMultiplier, SkillScalingBonus = sp.symbols('SkillMultiplier SkillScalingBonus')
#     bonusElementalDamage, bonusSkillDamage = sp.symbols('bonusElementalDamage bonusSkillDamage')
#     deepen, CriticalDamageMultiplier = sp.symbols('TotalDeepenEffect CriticalDamageMultiplier')
#     res_enemy, res_reduction = sp.symbols('EnemyResistance ResistanceReduction')
#     damage_formula = (
#         ((CharacterATK + WeaponATK) * (1 + bonusATK_percent) + bonus_flat_ATK)
#         * (SkillMultiplier * (1 + SkillScalingBonus))
#         * (1 + bonusElementalDamage + bonusSkillDamage)
#         * (1 + deepen)
#         * CriticalDamageMultiplier
#         * 0.48 * (1 - res_enemy + res_reduction)
#     )
#     return damage_formula
# damage_formula = define_damage_formula()

def simple_damage(character: Character, weapon: Weapon, move_id: str) -> tuple[float, float]:
    atk_base = character.base_atk() + weapon.base_atk()
    cd = character.cd()
    atk_bonus_prc = 0.00
    atk_bonus_flat = 0.00
    skill_scaling_mul = character.move_multiplier(move_id)
    skill_scaling_bonus = 0.00
    em_dmg_bonus = 0.00
    skill_dmg_bonus = 0.00
    deepen = 0.00
    res_enemy = 0.10
    res_reduction = 0.00
    dmg_noncrit = (
        (atk_base * (1.0 + atk_bonus_prc) + atk_bonus_flat) *
        skill_scaling_mul * (1.0 + skill_scaling_bonus) *
        (1.0 + em_dmg_bonus + skill_dmg_bonus) *
        (1.0 + deepen) *
        0.48 * (1 - res_enemy + res_reduction)
    )
    return dmg_noncrit, dmg_noncrit*cd

