class Moveset:
    def __init__(self):
        self.basic_attack = [
            {"name": "Part 1", "multiplier": 59.15},
            {"name": "Part 2", "multiplier": 76.05},
            {"name": "Part 3", "multiplier": 15.21 * 5},
            {"name": "Part 4", "multiplier": 130.13}
        ]
        self.heavy_attack = {"name": "Heavy Attack", "multiplier": 19.27 * 5}
        self.dodge_counter = {"name": "Dodge Counter", "multiplier": 195.34}
        self.ha_resonance = {"name": "HA Resonance", "multiplier": 76.058}
        self.ha_aftertune = {"name": "HA Aftertune", "multiplier": 126.75}
        self.midair_attack = {"name": "MidAir Attack", "multiplier": 104.78}
        self.resonance_skill = {"name": "Resonance Skill", "multiplier": 236.19}
        self.resonance_liberation = [
            {"name": "H1", "multiplier": 198.81},
            {"name": "H2", "multiplier": 675.96}
        ]
        self.intro_skill = {"name": "Intro Skill", "multiplier": 168.99}
        self.forte_circuit = [
            {"name": "Resonating Spin", "multiplier": 129.08 * 2},
            {"name": "Resonance Whirl", "multiplier": 39.77},
            {"name": "Resonating Echoes P1", "multiplier": 79.53},
            {"name": "Resonating Echoes P2", "multiplier": 159.05}
        ]
