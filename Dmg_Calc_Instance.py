import csv
import json
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
                print("Base HP: ", c.base_hp())
                print("Base ATK: ", c.base_atk())
                print("Base DEF: ", c.base_def())
                print(f"Crit Rate:  {c.cr*100:.1f}%")
                print(f"Crit Damage:  {c.cd*100:.1f}%")
                print("----------------------------")

    def display_weapon(self):
        print("Current weapon:")
        for w in self.build:
            if isinstance(w, Weapon):
                print("Weapon: ", w.name)
                print("Type: ", w.type)
                print("Flat ATK: ", w.base_atk())
                print(f"ATK Bonus: {w.substat()[1]:.1f}%")
                print("----------------------------")

def load_weapons_from_csv(file_path):
    weapons: list[Weapon] = []
    with open('data/weapons.json', mode='r') as weapons_json:
        weaps = json.load(weapons_json)
    for weapon_id in weaps:
        weapons.append(Weapon.by_id(weapon_id, level = 70))
    return weapons

def load_characters():
    characters: list[Character] = []
    with open('data/characters.json', mode='r') as chrs_json:
        chrs = json.load(chrs_json)
    for chr_id in chrs:
        characters.append(Character.by_id(chr_id, level = 90))
    return characters

def main():
    my_build = Build()

    # Load characters from CSV
    characters = load_characters()

    # Load weapons from CSV
    weapons = load_weapons_from_csv('data/weapons.csv')

    # Display character options
    print("Select a character:")
    for i, char in enumerate(characters):
        print(f"{1+i}. {char.name} (Level: {char.level}, HP: {char.base_hp()}, ATK: {char.base_atk()}, DEF: {char.base_def()})")

    char_choice = int(input("Enter the number of the character you want to select: ")) - 1
    selected_char = characters[char_choice]
    my_build.add_character(selected_char)
    my_build.display_character()

    # Display weapon options
    print("Select a weapon:")
    for i, weap in enumerate(weapons):
        print(f"{1+i}. {weap.name} (Type: {weap.type}, ATK: {weap.base_atk()}, ATK Bonus: {weap.substat()[1]*100}%)")

    weap_choice = int(input("Enter the number of the weapon you want to select: ")) - 1
    selected_weap = weapons[weap_choice]
    my_build.add_weapon(selected_weap)
    my_build.display_weapon()

    Base_Flat_Damage = selected_char.base_atk() + selected_weap.base_atk()
    Base_Flat_Bonus = 0.00
    Base_Attack_Bonus = 1.0 + selected_weap.substat()[1]
    Base_Attack = Base_Flat_Damage * Base_Attack_Bonus

    Crit_Rate = selected_char.cr
    Crit_Damage = selected_char.cd

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
