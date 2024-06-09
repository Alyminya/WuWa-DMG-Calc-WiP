import sympy as sp

class DamageCalculator:
    def __init__(self, base_attack, crit_damage, moveset):
        self.base_attack = base_attack
        self.crit_damage = crit_damage
        self.moveset = moveset
        self.results = {
            "Basic_Attack": [],
            "Heavy_Attack": None,
            "Dodge_Counter": None,
            "HA_Resonance": None,
            "HA_Aftertune": None,
            "MidAir_Attack": None,
            "Resonance_Skill": None,
            "Resonance_Liberation": [],
            "Intro_Skill": None,
            "Forte_Circuit": []
        }

    def calculate_single_attack_damage(self, multiplier):
        damage = self.base_attack * multiplier
        crit_damage_value = damage * (self.crit_damage)
        return {"damage": damage, "crit_damage": crit_damage_value}

    def calculate_damage(self):
        # Mapping move names to corresponding attributes in the moveset
        move_mappings = {
            "Heavy_Attack": self.moveset.heavy_attack,
            "Dodge_Counter": self.moveset.dodge_counter,
            "HA_Resonance": self.moveset.ha_resonance,
            "HA_Aftertune": self.moveset.ha_aftertune,
            "MidAir_Attack": self.moveset.midair_attack,
            "Resonance_Skill": self.moveset.resonance_skill,
            "Intro_Skill": self.moveset.intro_skill
        }

        for part in self.moveset.basic_attack:
            damage_result = self.calculate_single_attack_damage(part["multiplier"])
            self.results["Basic_Attack"].append({
                "name": part["name"],
                "damage": damage_result["damage"],
                "crit_damage": damage_result["crit_damage"]
            })

        for key, move in move_mappings.items():
            self.results[key] = self.calculate_single_attack_damage(move["multiplier"])

        for part in self.moveset.resonance_liberation:
            damage_result = self.calculate_single_attack_damage(part["multiplier"])
            self.results["Resonance_Liberation"].append({
                "name": part["name"],
                "damage": damage_result["damage"],
                "crit_damage": damage_result["crit_damage"]
            })

        for part in self.moveset.forte_circuit:
            damage_result = self.calculate_single_attack_damage(part["multiplier"])
            self.results["Forte_Circuit"].append({
                "name": part["name"],
                "damage": damage_result["damage"],
                "crit_damage": damage_result["crit_damage"]
            })

        return self.results

    @staticmethod
    def define_damage_formula():
        CharacterATK, WeaponATK, bonusATK_percent, bonus_flat_ATK = sp.symbols('CharacterATK WeaponATK bonusATK_percent bonus_flat_ATK')
        SkillMultiplier, SkillScalingBonus = sp.symbols('SkillMultiplier SkillScalingBonus')
        bonusElementalDamage, bonusSkillDamage = sp.symbols('bonusElementalDamage bonusSkillDamage')
        TotalDeepenEffect, CriticalDamageMultiplier = sp.symbols('TotalDeepenEffect CriticalDamageMultiplier')
        EnemyResistance, ResistanceReduction = sp.symbols('EnemyResistance ResistanceReduction')

        damage_formula = (
            (CharacterATK + WeaponATK) * (1 + bonusATK_percent) + bonus_flat_ATK
            * (SkillMultiplier * (1 + SkillScalingBonus))
            * (1 + bonusElementalDamage + bonusSkillDamage)
            * (1 + TotalDeepenEffect)
            * CriticalDamageMultiplier
            * 0.48 * (1 - EnemyResistance + ResistanceReduction)
        )

        return damage_formula
