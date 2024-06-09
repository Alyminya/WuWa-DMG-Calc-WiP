class Moveset:
    def __init__(self):
        self.basic_attack = [
            {"name": "Part 1", "multiplier": 0.5915},
            {"name": "Part 2", "multiplier": 0.7605},
            {"name": "Part 3", "multiplier": 0.1521 * 5},
            {"name": "Part 4", "multiplier": 1.3013}
        ]
        self.heavy_attack = {"name": "Heavy Attack", "multiplier": 1.927 * 5}
        self.dodge_counter = {"name": "Dodge Counter", "multiplier": 1.9534}
        self.ha_resonance = {"name": "HA Resonance", "multiplier": 0.76058}
        self.ha_aftertune = {"name": "HA Aftertune", "multiplier": 1.2675}
        self.midair_attack = {"name": "MidAir Attack", "multiplier": 1.0478}
        self.resonance_skill = {"name": "Resonance Skill", "multiplier": 2.3619}
        self.resonance_liberation = [
            {"name": "H1", "multiplier": 1.9881},
            {"name": "H2", "multiplier": 6.7596}
        ]
        self.intro_skill = {"name": "Intro Skill", "multiplier": 1.6899}
        self.forte_circuit = [
            {"name": "Resonating Spin", "multiplier": 1.2908 * 2},
            {"name": "Resonance Whirl", "multiplier": 0.3977},
            {"name": "Resonating Echoes P1", "multiplier": 0.7953},
            {"name": "Resonating Echoes P2", "multiplier": 1.5905}
        ]
