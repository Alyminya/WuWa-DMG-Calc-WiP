class Weapon:
    def __init__(self, name, type, flat_atk, atk_bonus):
        self.name = name
        self.type = type
        self.flat_atk = flat_atk
        self.atk_bonus = atk_bonus

    def __str__(self):
        return (f"Weapon({self.name}, Type: {self.type}, Flat ATK: {self.flat_atk}, "
                f"ATK Bonus: {self.atk_bonus}%)")
