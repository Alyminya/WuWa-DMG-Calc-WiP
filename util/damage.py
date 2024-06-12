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
    # Calculate the character stats
    base_atk = character.base_atk() + weapon.base_atk()
    atk = base_atk * (1 + weapon.substat()[1] + 0.04)
    # Calculate the Base DMG
    base_ability_dmg = atk * character.move_multiplier(move_id)
    flat_dmg = 0.00
    flat_bonus = 0.00
    base_dmg = base_ability_dmg + flat_dmg + flat_bonus
    # Calculate the resistances
    enemy_level = 65 # TODO(flysand): Enemy needs to come from parameters
    # TODO(flysand): The calculation for damage is still off by one with the current
    # test case. I need to verify everything, potentially re-derive the formula
    # for damage for which I'll need lots of testing.
    enemy_base_res = 0.1
    res_penetration = 0.0
    res_total = enemy_base_res + res_penetration
    em_res = \
        (1 - res_total/2) if res_total < 0 else \
        (1 - res_total) if res_total < 0.8 else \
        (1 / (1+5*res_total))
    enemy_def = 8*enemy_level + 792
    enemy_def_ign = 0
    def_mul = (800+8*character.level) / (800+8*character.level + enemy_def * (1 - enemy_def_ign))
    dmg_reduction = 1.0
    resistance = em_res * def_mul * dmg_reduction
    # resistance = 0.46
    print(resistance, res_total, em_res, def_mul, dmg_reduction)
    # Calculate bonuses
    dmg_bonus = 1 + character.em_bonus()
    dmg_amplify = 1 + 0
    bonuses = dmg_bonus * dmg_amplify
    # Calcualte crit and noncrit damage
    dmg_noncrit = base_dmg * resistance * bonuses
    return dmg_noncrit, dmg_noncrit*character.stat('cd')
