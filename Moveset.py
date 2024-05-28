class Moveset:
    def __init__(
        self,
        basic_attack,
        heavy_attack,
        dodge_counter,
        ha_resonance,
        ha_aftertune,
        midair_attack,
        resonance_skill,
        resonance_liberation,
        intro_skill,
        outro_skill,
        forte_circuit,
    ):
        self.basic_attack = basic_attack
        self.heavy_attack = heavy_attack
        self.dodge_counter = dodge_counter
        self.ha_resonance = ha_resonance
        self.ha_aftertune = ha_aftertune
        self.midair_attack = midair_attack
        self.resonance_skill = resonance_skill
        self.resonance_liberation = resonance_liberation
        self.intro_skill = intro_skill
        self.outro_skill = outro_skill
        self.forte_circuit = forte_circuit

    def calculate_damage(self, base_attack, crit_damage):
        results = {}

        # Basic Attack
        results["Basic_Attack"] = []
        for part in self.basic_attack:
            damage = base_attack * (part["multiplier"] / 100)
            crit_damage_value = damage * (crit_damage / 100)
            results["Basic_Attack"].append(
                {
                    "name": part["name"],
                    "damage": damage,
                    "crit_damage": crit_damage_value,
                }
            )

        # Heavy Attack
        results["Heavy_Attack"] = {
            "damage": base_attack * (self.heavy_attack["multiplier"] / 100),
            "crit_damage": base_attack
            * (self.heavy_attack["multiplier"] / 100)
            * (crit_damage / 100),
        }

        # Dodge Counter
        results["Dodge_Counter"] = {
            "damage": base_attack * (self.dodge_counter["multiplier"] / 100),
            "crit_damage": base_attack
            * (self.dodge_counter["multiplier"] / 100)
            * (crit_damage / 100),
        }

        # HA Resonance
        results["HA_Resonance"] = {
            "damage": base_attack * (self.ha_resonance["multiplier"] / 100),
            "crit_damage": base_attack
            * (self.ha_resonance["multiplier"] / 100)
            * (crit_damage / 100),
        }

        # HA Aftertune
        results["HA_Aftertune"] = {
            "damage": base_attack * (self.ha_aftertune["multiplier"] / 100),
            "crit_damage": base_attack
            * (self.ha_aftertune["multiplier"] / 100)
            * (crit_damage / 100),
        }

        # MidAir Attack
        results["MidAir_Attack"] = {
            "damage": base_attack * (self.midair_attack["multiplier"] / 100),
            "crit_damage": base_attack
            * (self.midair_attack["multiplier"] / 100)
            * (crit_damage / 100),
        }

        # Resonance Skill
        results["Resonance_Skill"] = {
            "damage": base_attack * (self.resonance_skill["multiplier"] / 100),
            "crit_damage": base_attack
            * (self.resonance_skill["multiplier"] / 100)
            * (crit_damage / 100),
        }

        # Resonance Liberation
        results["Resonance_Liberation"] = []
        for part in self.resonance_liberation:
            damage = base_attack * (part["multiplier"] / 100)
            crit_damage_value = damage * (crit_damage / 100)
            results["Resonance_Liberation"].append(
                {
                    "name": part["name"],
                    "damage": damage,
                    "crit_damage": crit_damage_value,
                }
            )

        # Intro Skill
        results["Intro_Skill"] = {
            "damage": base_attack * (self.intro_skill["multiplier"] / 100),
            "crit_damage": base_attack
            * (self.intro_skill["multiplier"] / 100)
            * (crit_damage / 100),
        }

        # Outro Skill
        results["Outro_Skill"] = {
            "damage": base_attack * (self.outro_skill["multiplier"] / 100),
            "crit_damage": base_attack
            * (self.outro_skill["multiplier"] / 100)
            * (crit_damage / 100),
        }

        # Forte Circuit
        results["Forte_Circuit"] = []
        for part in self.forte_circuit:
            damage = base_attack * (part["multiplier"] / 100)
            crit_damage_value = damage * (crit_damage / 100)
            results["Forte_Circuit"].append(
                {
                    "name": part["name"],
                    "damage": damage,
                    "crit_damage": crit_damage_value,
                }
            )

        return results
