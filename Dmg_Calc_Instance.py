import csv
from util.character import Character
from util.weapon import Weapon
from util.moveset import Moveset
from util.damage_instance import DamageCalculator

class Build:
    def __init__(self):
        self.build = []

    def add_character(self, built_character):
        self.build.append(built_character)

    def add_weapon(self, built_weapon):
        self.build.append(built_weapon)

    def display_character(self):
        print("Current character:")
        for c in self.build:
            if isinstance(c, Character):
                print("Character: ", c.name)
                print("Level: ", c.level)
                print("HP: ", c.hp)
                print("ATK: ", c.atk)
                print("DEF: ", c.defense)
                print(f"Crit Rate:  {c.crit_rate:.1f}%")
                print(f"Crit Damage:  {c.crit_dmg:.1f}%")
                print("----------------------------")

    def display_weapon(self):
        print("Current weapon:")
        for w in self.build:
            if isinstance(w, Weapon):
                print("Weapon: ", w.name)
                print("Type: ", w.type)
                print("Flat ATK: ", w.flat_atk)
                print(f"ATK Bonus: {w.atk_bonus:.1f}%")
                print("----------------------------")

def load_weapons_from_csv(file_path):
    weapons = []
    with open(file_path, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            weapons.append(Weapon(
                name=row['name'],
                type=row['type'],
                flat_atk=float(row['flat_atk']),
                atk_bonus=float(row['atk_bonus'])
            ))
    return weapons

def load_characters_from_csv(file_path):
    characters = []
    with open(file_path, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            characters.append(Character(
                name=row['name'],
                level=int(row['level']),
                hp=float(row['hp']),
                atk=float(row['atk']),
                defense=float(row['defense']),
                crit_rate=float(row['crit_rate']),
                crit_dmg=float(row['crit_dmg'])
            ))
    return characters

def main():
    my_build = Build()

    # Load characters from CSV
    characters = load_characters_from_csv('data/characters.csv')

    # Load weapons from CSV
    weapons = load_weapons_from_csv('data/weapons.csv')

    # Display character options
    print("Select a character:")
    for i, char in enumerate(characters):
        print(f"{i + 1}. {char.name} (Level: {char.level}, HP: {char.hp}, ATK: {char.atk}, DEF: {char.defense}, Crit Rate: {char.crit_rate}%, Crit Damage: {char.crit_dmg}%)")

    char_choice = int(input("Enter the number of the character you want to select: ")) - 1
    selected_char = characters[char_choice]
    my_build.add_character(selected_char)
    my_build.display_character()

    # Display weapon options
    print("Select a weapon:")
    for i, weap in enumerate(weapons):
        print(f"{i + 1}. {weap.name} (Type: {weap.type}, Flat ATK: {weap.flat_atk}, ATK Bonus: {weap.atk_bonus}%)")

    weap_choice = int(input("Enter the number of the weapon you want to select: ")) - 1
    selected_weap = weapons[weap_choice]
    my_build.add_weapon(selected_weap)
    my_build.display_weapon()

    Base_Flat_Damage = selected_char.atk + selected_weap.flat_atk
    Base_Flat_Bonus = 0.00
    Base_Attack_Bonus = 1 + (selected_weap.atk_bonus / 100)
    Base_Attack = Base_Flat_Damage * Base_Attack_Bonus

    Crit_Rate = selected_char.crit_rate
    Crit_Damage = selected_char.crit_dmg

    moveset = Moveset()
    calculator = DamageCalculator(Base_Attack, Crit_Damage, moveset)
    damage_results = calculator.calculate_damage()

    for attack_type, attacks in damage_results.items():
        print(attack_type + ":")
        if isinstance(attacks, list):
            for attack in attacks:
                print(f"{attack['name']} damage: {attack['damage']:.2f}")
                print(f"{attack['name']} crit damage: {attack['crit_damage']:.2f}")
        else:
            print(f"Damage: {attacks['damage']:.2f}")
            print(f"Crit damage: {attacks['crit_damage']:.2f}")
        print("---------------------------")

if __name__ == "__main__":
    main()
