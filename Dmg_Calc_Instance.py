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

class MoveDesc:
    character_id: str
    move_id: str
    def __init__(self, character_id: str, move_id: str) -> None:
        self.character_id = character_id
        self.move_id = move_id

class TeamBuild:
    team: dict
    rotation: list[MoveDesc]

    def __init__(self) -> None:
        self.team = {}
        self.rotation = []

    def add_character(self, built_character: Character) -> None:
        self.team[built_character.info.id] = built_character

    def add_weapon(self, built_weapon: Weapon, character_id: str) -> None:
        if character_id in self.team:
            self.team[character_id].weapon = built_weapon
    
    def add_move(self, move: MoveDesc) -> None:
        self.rotation.append(move)

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
            row_list: list[list[str]] = []
            for move_id in character.moves():
                non_crit, crit = util.damage.simple_damage(character, character.weapon, move_id)
                row_list.append(
                    [character.info.moves[move_id].name, f'{non_crit:.2f}', f'{crit:.2f}']
                )
            print(character_info)
            print(tabulate(row_list, headers=headers))
    
    def display_rotation(self) -> None:
        headers = ["Character", "Attack", "Non-Crit", "Crit"]
        row_list: list[list[str]] = []
        for move_desc in self.rotation:
            character = self.team[move_desc.character_id]
            non_crit, crit = util.damage.simple_damage(character, character.weapon, move_desc.move_id)
            row_list.append(
                [character.info.name, character.info.moves[move_desc.move_id].name, f'{non_crit:.2f}', f'{crit:.2f}']
            )
        print(tabulate(row_list, headers=headers))

def main_file(json_data: dict) -> None:
    test_build = TeamBuild()
    for character, info in json_data["characters"].items():
        test_build.add_character(Character(character, level = info["level"], forte_levels = info["forte_levels"]))
        test_build.add_weapon(Weapon(info["weapon"]["weapon_id"], level = info["weapon"]["level"]), character)
        for move in json_data["rotation"]:
            if move["type"] == "move":
                test_build.add_move(MoveDesc(move["character"], move["move"]))
    test_build.display_rotation()

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
