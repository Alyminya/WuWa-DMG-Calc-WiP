from util.character import Character
from util.weapon import Weapon

import util.damage
import util.db
import util.db.model

class Build:
    def __init__(self) -> type(self):
        self.build = []

    def add_character(self, built_character: Character) -> None:
        self.build.append(built_character)

    def add_weapon(self, built_weapon: Weapon) -> None:
        self.build.append(built_weapon)

    def display_character(self: type(self)) -> None:
        print("Current character:")
        for c in self.build:
            if isinstance(c, Character):
                print("Character: ", c.info.name)
                print("Level: ", c.level)
                print("Base HP: ", c.base_hp())
                print("Base ATK: ", c.base_atk())
                print("Base DEF: ", c.base_def())
                print(f"Crit Rate:  {c.cr()*100:.1f}%")
                print(f"Crit Damage:  {c.cd()*100:.1f}%")
                print("----------------------------")

    def display_weapon(self: type(self)) -> None:
        print("Current weapon:")
        for w in self.build:
            if isinstance(w, Weapon):
                print("Weapon: ", w.info.name)
                print("Type: ", w.info.type)
                print("Flat ATK: ", w.base_atk())
                print(f"ATK Bonus: {w.substat()[1]:.1f}%")
                print("----------------------------")

def load_weapons(weapon_type: util.db.model.Weapon_Type) -> list[Weapon]:
    weapons: list[Weapon] = []
    for weapon_id in util.db.data.weapons:
        weapon = Weapon(weapon_id, level = 70)
        if weapon.info.type == weapon_type:
            weapons.append(weapon)
    return weapons

def load_characters() -> list[Character]:
    default_forte: dict[util.db.Forte_Type, int] = {
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
    for attack_id in selected_char.attacks():
        attack = selected_char.info.attacks[attack_id]
        non_crit_dmg, crit_dmg = util.damage.simple_damage(selected_char, selected_weap, attack_id)
        print(attack.name, ":", (60-len(attack.name)-1)*' ', f'{non_crit_dmg:>12.2f}', " ", f'{crit_dmg:>12.2f}', sep="")

if __name__ == "__main__":
    main()
