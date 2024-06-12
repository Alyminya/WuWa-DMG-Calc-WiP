import sys
import json

from tabulate import tabulate

from util.character import Character
from util.weapon import Weapon

import util.damage
import util.db
import util.db.model

class Build:

    build: list[Character|Weapon]

    def __init__(self) -> None:
        self.build = []

    def add_character(self, built_character: Character) -> None:
        self.build.append(built_character)

    def add_weapon(self, built_weapon: Weapon) -> None:
        self.build.append(built_weapon)

    def display_character(self) -> None:
        print("Current character:")
        for c in self.build:
            if isinstance(c, Character):
                print("Character: ", c.info.name)
                print("Level: ", c.level)
                print("Base HP: ", c.base_hp())
                print("Base ATK: ", c.base_atk())
                print("Base DEF: ", c.base_def())
                print(f"Crit Rate:  {c.stat('cr')*100:.1f}%")
                print(f"Crit Damage:  {c.stat('cd')*100:.1f}%")
                print("----------------------------")

    def display_weapon(self) -> None:
        print("Current weapon:")
        for w in self.build:
            if isinstance(w, Weapon):
                print("Weapon: ", w.info.name)
                print("Type: ", w.info.type)
                print("Flat ATK: ", w.base_atk())
                print(f"ATK Bonus: {w.substat()[1]:.1f}%")
                print("----------------------------")

class TeamBuild:
    team: dict
    def __init__(self) -> None:
        self.team = {}

    def add_character(self, built_character: Character) -> None:
        self.team[built_character.info.id] = built_character

    def add_weapon(self, built_weapon: Weapon, character_id: str) -> None:
        if character_id in self.team:
            self.team[character_id].weapon = built_weapon

    def display_team(self) -> None:
        for chr_id, character in self.team.items():
            character_info = f"""
Character:  {character.info.name}
    Level:          {character.level}
    Base HP:        {character.base_hp()}
    Base DEF:       {character.base_def()}
    Base ATK:       {character.base_atk()}
    Crit Rate:      {character.stat('cr')*100:.1f}%
    Crit Damage:    {character.stat('cd')*100:.1f}%
    Weapon:         {character.weapon.info.name}
        Weapon Type:    {character.weapon.info.type}
        Base Attack:    {character.weapon.base_atk()}
        Substat:        {character.weapon.substat()[1]:.1f}% {character.weapon.substat()[0]}
            """
            
            headers = ["Attack", "Non-Crit", "Crit"]
            row_list = []
            for move_id in character.moves():
                non_crit, crit = util.damage.simple_damage(character, character.weapon, move_id)
                row_list.append(
                    [character.info.moves[move_id].name, f'{non_crit:.0f}', f'{crit:.0f}']
                )
            print(character_info)
            print(tabulate(row_list, headers=headers))

def load_weapons(weapon_type: util.db.model.Weapon_Type) -> list[Weapon]:
    weapons: list[Weapon] = []
    for weapon_id in util.db.data.weapons:
        weapon = Weapon(weapon_id, level = 70)
        if weapon.info.type == weapon_type:
            weapons.append(weapon)
    return weapons

def load_characters() -> list[Character]:
    default_forte: dict[util.db.model.Forte_Type, int] = {
        'a': 10,
        'e': 10,
        'f': 10,
        'r': 10,
        'i': 10,
    }
    characters: list[Character] = []
    for chr_id in util.db.data.characters:
        characters.append(Character(chr_id, level = 90, forte_levels = default_forte))
    return characters

def main() -> None:
    my_build = Build()
    characters = load_characters()

    # Display character options
    print("Select a character:")
    for i, char in enumerate(characters):
        print(f"{1+i}. {char.info.name} (Level: {char.level}, HP: {char.base_hp()}, ATK: {char.base_atk()}, DEF: {char.base_def()})")

    char_choice = int(input("Enter the number of the character you want to select: ")) - 1
    selected_char = characters[char_choice]
    my_build.add_character(selected_char)
    my_build.display_character()

    # Display weapon options
    print("Select a weapon:")
    weapons = load_weapons(selected_char.info.weapon)
    for i, weap in enumerate(weapons):
        print(f"{1+i}. {weap.info.name} (Type: {weap.info.type}, ATK: {weap.base_atk()}, ATK Bonus: {weap.substat()[1]*100}%)")

    weap_choice = int(input("Enter the number of the weapon you want to select: ")) - 1
    selected_weap = weapons[weap_choice]
    my_build.add_weapon(selected_weap)
    my_build.display_weapon()

    print()
    print('Attack', (60-len('Attack'))*' ', ' non-crit     ', 'crit', sep='')
    print('-'*60, ' ', '-'*12, ' ', '-'*12, sep='')
    for move_id in selected_char.moves():
        move = selected_char.info.moves[move_id]
        non_crit_dmg, crit_dmg = util.damage.simple_damage(selected_char, selected_weap, move_id)
        print(move.name, ":", (60-len(move.name)-1)*' ', f'{non_crit_dmg:>12.2f}', " ", f'{crit_dmg:>12.2f}', sep="")

def main_file(json_data: dict) -> None:
    test_build = TeamBuild()
    for character, info in json_data["characters"].items():
        test_build.add_character(Character(character, level = info["level"], forte_levels = info["forte_levels"]))
        test_build.add_weapon(Weapon(info["weapon"]["weapon_id"], level = info["weapon"]["level"]), character)
    test_build.display_team()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-f":
        if len(sys.argv) < 3:
            print(f'{sys.argv[0]} -f <file.json>')
        json_file = sys.argv[2]
        with open(json_file, "r") as f:
            json_data = json.load(f)
        main_file(json_data)
    else:
        print(f'{sys.argv[0]} -f <file.json>')
