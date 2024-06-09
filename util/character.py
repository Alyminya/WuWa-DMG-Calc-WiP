import csv

class Character:
    def __init__(self, name, level, hp, atk, defense, crit_rate, crit_dmg):
        self.name = name
        self.level = level
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.crit_rate = crit_rate
        self.crit_dmg = crit_dmg

    @classmethod
    def from_csv(cls, name, file_path):
        """Load character data from a CSV file."""
        with open(file_path, mode='r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                if row['name'] == name:
                    return cls(
                        name=row['name'],
                        level=int(row['level']),
                        hp=float(row['hp']),
                        atk=float(row['atk']),
                        defense=float(row['defense']),
                        crit_rate=float(row['crit_rate']),
                        crit_dmg=float(row['crit_dmg'])
                    )
        raise ValueError(f"Character {name} not found in {file_path}")

    def update_stats(self, **kwargs):
        """Update character stats."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"{key} is not a valid attribute of Character")

    def __str__(self):
        """String representation of the character."""
        return (f"Character({self.name}, Level: {self.level}, HP: {self.hp}, "
                f"ATK: {self.atk}, DEF: {self.defense}, Crit Rate: {self.crit_rate}%, "
                f"Crit Damage: {self.crit_dmg}%)")
