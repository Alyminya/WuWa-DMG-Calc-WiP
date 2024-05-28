from Characters import character
from Weapons import weapon


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
            if isinstance(c, character):
                print("Character: ", c.CharName)
                print("Level: ", c.CLevel)
                print("HP: ", c.CHP)
                print("ATK: ", c.CATK)
                print("DEF: ", c.CDEF)
                print(f"Crit Rate:  {c.CCRate:.1f}%")
                print(f"Crit Damage:  {c.CCDMG:.1f}%")
                print("----------------------------")

    def display_weapon(self):
        print("Current weapon:")
        for w in self.build:
            if isinstance(w, weapon):
                print("Weapon: ", w.WName)
                print("Type: ", w.WType)
                print("Flat ATK: ", w.WFlatATK)
                print(f"ATK Bonus: {w.WATKBonus:.1f}%")
                print("----------------------------")


def main():
    my_build = Build()

    # Predefined characters
    characters = [
        character("Spectro Rover", 90, 12312.00, 405.00, 1480.89, 5.00, 150.00),
        character("Yangyang", 90, 11016.00, 270.00, 1190.00, 5.00, 150.00),
        character("Chixia", 90, 9814.50, 324.00, 1031.33, 5.00, 150.00),
        character("Sanhua", 90, 10867.50, 297.00, 1018.11, 5.00, 150.00),
        character("Taoqi", 90, 9666.00, 243.00, 1692.44, 5.00, 150.00),
        character("Baizhi", 90, 13837.50, 229.50, 1084.22, 5.00, 150.00),
        character("Danjin", 90, 10192.50, 283.50, 1242.89, 5.00, 150.00),
        character("Aalto", 90, 10638.00, 283.50, 1163.55, 5.00, 150.00),
        character("Mortefi", 90, 10827.00, 270.00, 1229.66, 5.00, 150.00),
        character("Yuanwu", 90, 9207.00, 243.00, 1771.77, 5.00, 150.00),
        character("Verina", 90, 15376.50, 364.50, 1190.00, 5.00, 150.00),
        character("Encore", 90, 11353.50, 459.00, 1348.66, 5.00, 150.00),
        character("Calcharo", 90, 11340.00, 472.50, 1282.55, 5.00, 150.00),
        character("Lingyang", 90, 11218.50, 472.50, 1309.00, 5.00, 150.00),
        character("Jianxin", 90, 15241.50, 364.50, 1216.44, 5.00, 150.00),
        character("Jiyan", 90, 11326.50, 472.50, 1282.55, 5.00, 150.00),
        character("Yinlin", 90, 11880.00, 432.00, 1388.33, 5.00, 150.00),
    ]

    weapons = {
        "Spectro Rover": [
            weapon("Training Sword", "Sword", 250.00, 11.47),
            weapon("Tyro Sword", "Sword", 275.00, 14.85),
            weapon("Guardian Sword", "Sword", 300.00, 30.38),
            weapon("Sword of Voyager", "Sword", 300.00, 0.00),
            weapon("Originite: Type II", "Sword", 325.00, 24.30),
            weapon("Sword of Night", "Sword", 350.00, 24.30),
            weapon("Lumingloss", "Sword", 387.50, 36.45),
            weapon("Lunar Cutter", "Sword", 412.50, 30.38),
            weapon("Commando of Conviction", "Sword", 412.50, 30.38),
            weapon("Sword#18", "Sword", 387.50, 36.45),
            weapon("Scale: Slasher", "Sword", 337.50, 0.00),
            weapon("Emerald of Genesis", "Sword", 587.50, 0.00),
        ],
        "Yangyang": [
            weapon("Training Sword", "Sword", 250.00, 11.47),
            weapon("Tyro Sword", "Sword", 275.00, 14.85),
            weapon("Guardian Sword", "Sword", 300.00, 30.38),
            weapon("Sword of Voyager", "Sword", 300.00, 0.00),
            weapon("Originite: Type II", "Sword", 325.00, 24.30),
            weapon("Sword of Night", "Sword", 350.00, 24.30),
            weapon("Lumingloss", "Sword", 387.50, 36.45),
            weapon("Lunar Cutter", "Sword", 412.50, 30.38),
            weapon("Commando of Conviction", "Sword", 412.50, 30.38),
            weapon("Sword#18", "Sword", 387.50, 36.45),
            weapon("Scale: Slasher", "Sword", 337.50, 0.00),
            weapon("Emerald of Genesis", "Sword", 587.50, 0.00),
        ],
        "Chixia": [
            weapon("Training Pistols", "Pistols", 250.00, 11.47),
            weapon("Tyro Pistols", "Pistols", 275.00, 14.85),
            weapon("Pistols of Voyager", "Pistols", 300.00, 30.38),
            weapon("Originite: Type III", "Pistols", 325.00, 24.30),
            weapon("Guardian Pistols", "Pistols", 300.00, 30.38),
            weapon("Pistols of Night", "Pistols", 325.00, 24.30),
            weapon("Thunderbolt", "Pistols", 387.50, 36.45),
            weapon("Pistols#26", "Pistols", 387.50, 36.45),
            weapon("Novaburst", "Pistols", 412.50, 30.38),
            weapon("Undying Flame", "Pistols", 412.50, 30.38),
            weapon("Cadenza", "Pistols", 337.50, 0.00),
            weapon("Static Mist", "Pistols", 587.50, 0.00),
        ],
        "Sanhua": [
            weapon("Training Sword", "Sword", 250.00, 11.47),
            weapon("Tyro Sword", "Sword", 275.00, 14.85),
            weapon("Guardian Sword", "Sword", 300.00, 30.38),
            weapon("Sword of Voyager", "Sword", 300.00, 0.00),
            weapon("Originite: Type II", "Sword", 325.00, 24.30),
            weapon("Sword of Night", "Sword", 350.00, 24.30),
            weapon("Lumingloss", "Sword", 387.50, 36.45),
            weapon("Lunar Cutter", "Sword", 412.50, 30.38),
            weapon("Commando of Conviction", "Sword", 412.50, 30.38),
            weapon("Sword#18", "Sword", 387.50, 36.45),
            weapon("Scale: Slasher", "Sword", 337.50, 0.00),
            weapon("Emerald of Genesis", "Sword", 587.50, 0.00),
        ],
        "Taoqi": [
            weapon("Training Broadblade", "Broadblade", 250.00, 11.47),
            weapon("Tyro Broadblade", "Broadblade", 275.00, 14.85),
            weapon("Guardian Broadblade", "Broadblade", 325.00, 24.30),
            weapon("Broadblade of Voyager", "Broadblade", 300.00, 0.00),
            weapon("Originite: Type I", "Broadblade", 325.00, 0.00),
            weapon("Broadblade of Night", "Broadblade", 325.00, 24.30),
            weapon("Autumntrace", "Broadblade", 387.50, 0.00),
            weapon("Helios Cleaver", "Broadblade", 412.50, 30.38),
            weapon("Dauntless Evernight", "Broadblade", 337.50, 0.00),
            weapon("Broadblade#41", "Broadblade", 412.50, 0.00),
            weapon("Discord", "Broadblade", 337.50, 0.00),
            weapon("Lustrous Razor", "Broadblade", 587.50, 36.45),
            weapon("Verdant Summit", "Broadblade", 587.50, 0.00),
        ],
        "Baizhi": [
            weapon("Training Rectifier", "Rectifier", 250.00, 11.47),
            weapon("Tyro Rectifier", "Rectifier", 275.00, 14.85),
            weapon("Guardian Rectifier", "Rectifier", 325.00, 24.30),
            weapon("Rectifier of Voyager", "Rectifier", 300.00, 0.00),
            weapon("Originite: Type V", "Rectifier", 300.00, 0.00),
            weapon("Rectifier of Night", "Rectifier", 325.00, 24.30),
            weapon("Augment", "Rectifier", 412.50, 0.00),
            weapon("Comet Flare", "Rectifier", 412.50, 0.00),
            weapon("Jinzhou Keeper", "Rectifier", 387.50, 36.45),
            weapon("Rectifier#25", "Rectifier", 337.50, 0.00),
            weapon("Variation", "Rectifier", 337.50, 0.00),
            weapon("Cosmic Ripples", "Rectifier", 500.00, 54.00),
            weapon("Stringmaster", "Rectifier", 500.00, 0.00),
        ],
        "Danjin": [
            weapon("Training Sword", "Sword", 250.00, 11.47),
            weapon("Tyro Sword", "Sword", 275.00, 14.85),
            weapon("Guardian Sword", "Sword", 300.00, 30.38),
            weapon("Sword of Voyager", "Sword", 300.00, 0.00),
            weapon("Originite: Type II", "Sword", 325.00, 24.30),
            weapon("Sword of Night", "Sword", 350.00, 24.30),
            weapon("Lumingloss", "Sword", 387.50, 36.45),
            weapon("Lunar Cutter", "Sword", 412.50, 30.38),
            weapon("Commando of Conviction", "Sword", 412.50, 30.38),
            weapon("Sword#18", "Sword", 387.50, 36.45),
            weapon("Scale: Slasher", "Sword", 337.50, 0.00),
            weapon("Emerald of Genesis", "Sword", 587.50, 0.00),
        ],
        "Aalto": [
            weapon("Training Pistols", "Pistols", 250.00, 11.47),
            weapon("Tyro Pistols", "Pistols", 275.00, 14.85),
            weapon("Pistols of Voyager", "Pistols", 300.00, 30.38),
            weapon("Originite: Type III", "Pistols", 325.00, 24.30),
            weapon("Guardian Pistols", "Pistols", 300.00, 30.38),
            weapon("Pistols of Night", "Pistols", 325.00, 24.30),
            weapon("Thunderbolt", "Pistols", 387.50, 36.45),
            weapon("Pistols#26", "Pistols", 387.50, 36.45),
            weapon("Novaburst", "Pistols", 412.50, 30.38),
            weapon("Undying Flame", "Pistols", 412.50, 30.38),
            weapon("Cadenza", "Pistols", 337.50, 0.00),
            weapon("Static Mist", "Pistols", 587.50, 0.00),
        ],
        "Mortefi": [
            weapon("Training Pistols", "Pistols", 250.00, 11.47),
            weapon("Tyro Pistols", "Pistols", 275.00, 14.85),
            weapon("Pistols of Voyager", "Pistols", 300.00, 30.38),
            weapon("Originite: Type III", "Pistols", 325.00, 24.30),
            weapon("Guardian Pistols", "Pistols", 300.00, 30.38),
            weapon("Pistols of Night", "Pistols", 325.00, 24.30),
            weapon("Thunderbolt", "Pistols", 387.50, 36.45),
            weapon("Pistols#26", "Pistols", 387.50, 36.45),
            weapon("Novaburst", "Pistols", 412.50, 30.38),
            weapon("Undying Flame", "Pistols", 412.50, 30.38),
            weapon("Cadenza", "Pistols", 337.50, 0.00),
            weapon("Static Mist", "Pistols", 587.50, 0.00),
        ],
        "Yuanwu": [
            weapon("Training Gauntlets", "Gauntlets", 250.00, 11.47),
            weapon("Tyro Gauntlets", "Gauntlets", 275.00, 14.85),
            weapon("Gauntlets of Voyager", "Gauntlets", 325.00, 0.00),
            weapon("Originite: Type IV", "Gauntlets", 300.00, 0.00),
            weapon("Guardian Gauntlets", "Gauntlets", 300.00, 0.00),
            weapon("Gauntlets of Night", "Gauntlets", 325.00, 24.30),
            weapon("Hollow Mirage", "Gauntlets", 412.50, 30.38),
            weapon("Stonard", "Gauntlets", 412.50, 0.00),
            weapon("Gauntlets#21D", "Gauntlets", 387.50, 0.00),
            weapon("Amity Record", "Gauntlets", 337.50, 0.00),
            weapon("Marcato", "Gauntlets", 337.50, 0.00),
            weapon("Abyss Surges", "Gauntlets", 587.50, 36.45),
        ],
        "Verina": [
            weapon("Training Rectifier", "Rectifier", 250.00, 11.47),
            weapon("Tyro Rectifier", "Rectifier", 275.00, 14.85),
            weapon("Guardian Rectifier", "Rectifier", 325.00, 24.30),
            weapon("Rectifier of Voyager", "Rectifier", 300.00, 0.00),
            weapon("Originite: Type V", "Rectifier", 300.00, 0.00),
            weapon("Rectifier of Night", "Rectifier", 325.00, 24.30),
            weapon("Augment", "Rectifier", 412.50, 0.00),
            weapon("Comet Flare", "Rectifier", 412.50, 0.00),
            weapon("Jinzhou Keeper", "Rectifier", 387.50, 36.45),
            weapon("Rectifier#25", "Rectifier", 337.50, 0.00),
            weapon("Variation", "Rectifier", 337.50, 0.00),
            weapon("Cosmic Ripples", "Rectifier", 500.00, 54.00),
            weapon("Stringmaster", "Rectifier", 500.00, 0.0),
        ],
        "Encore": [
            weapon("Training Rectifier", "Rectifier", 250.00, 11.47),
            weapon("Tyro Rectifier", "Rectifier", 275.00, 14.85),
            weapon("Guardian Rectifier", "Rectifier", 325.00, 24.30),
            weapon("Rectifier of Voyager", "Rectifier", 300.00, 0.00),
            weapon("Originite: Type V", "Rectifier", 300.00, 0.00),
            weapon("Rectifier of Night", "Rectifier", 325.00, 24.30),
            weapon("Augment", "Rectifier", 412.50, 0.00),
            weapon("Comet Flare", "Rectifier", 412.50, 0.00),
            weapon("Jinzhou Keeper", "Rectifier", 387.50, 36.45),
            weapon("Rectifier#25", "Rectifier", 337.50, 0.00),
            weapon("Variation", "Rectifier", 337.50, 0.00),
            weapon("Cosmic Ripples", "Rectifier", 500.00, 54.00),
            weapon("Stringmaster", "Rectifier", 500.00, 0.0),
        ],
        "Calcharo": [
            weapon("Training Broadblade", "Broadblade", 250.00, 11.47),
            weapon("Tyro Broadblade", "Broadblade", 275.00, 14.85),
            weapon("Guardian Broadblade", "Broadblade", 325.00, 24.30),
            weapon("Broadblade of Voyager", "Broadblade", 300.00, 0.00),
            weapon("Originite: Type I", "Broadblade", 325.00, 0.00),
            weapon("Broadblade of Night", "Broadblade", 325.00, 24.30),
            weapon("Autumntrace", "Broadblade", 387.50, 0.00),
            weapon("Helios Cleaver", "Broadblade", 412.50, 30.38),
            weapon("Dauntless Evernight", "Broadblade", 337.50, 0.00),
            weapon("Broadblade#41", "Broadblade", 412.50, 0.00),
            weapon("Discord", "Broadblade", 337.50, 0.00),
            weapon("Lustrous Razor", "Broadblade", 587.50, 36.45),
            weapon("Verdant Summit", "Broadblade", 587.50, 0.00),
        ],
        "Lingyang": [
            weapon("Training Gauntlets", "Gauntlets", 250.00, 11.47),
            weapon("Tyro Gauntlets", "Gauntlets", 275.00, 14.85),
            weapon("Gauntlets of Voyager", "Gauntlets", 325.00, 0.00),
            weapon("Originite: Type IV", "Gauntlets", 300.00, 0.00),
            weapon("Guardian Gauntlets", "Gauntlets", 300.00, 0.00),
            weapon("Gauntlets of Night", "Gauntlets", 325.00, 24.30),
            weapon("Hollow Mirage", "Gauntlets", 412.50, 30.38),
            weapon("Stonard", "Gauntlets", 412.50, 0.00),
            weapon("Gauntlets#21D", "Gauntlets", 387.50, 0.00),
            weapon("Amity Record", "Gauntlets", 337.50, 0.00),
            weapon("Marcato", "Gauntlets", 337.50, 0.00),
            weapon("Abyss Surges", "Gauntlets", 587.50, 36.45),
        ],
        "Jianxin": [
            weapon("Training Gauntlets", "Gauntlets", 250.00, 11.47),
            weapon("Tyro Gauntlets", "Gauntlets", 275.00, 14.85),
            weapon("Gauntlets of Voyager", "Gauntlets", 325.00, 0.00),
            weapon("Originite: Type IV", "Gauntlets", 300.00, 0.00),
            weapon("Guardian Gauntlets", "Gauntlets", 300.00, 0.00),
            weapon("Gauntlets of Night", "Gauntlets", 325.00, 24.30),
            weapon("Hollow Mirage", "Gauntlets", 412.50, 30.38),
            weapon("Stonard", "Gauntlets", 412.50, 0.00),
            weapon("Gauntlets#21D", "Gauntlets", 387.50, 0.00),
            weapon("Amity Record", "Gauntlets", 337.50, 0.00),
            weapon("Marcato", "Gauntlets", 337.50, 0.00),
            weapon("Abyss Surges", "Gauntlets", 587.50, 36.45),
        ],
        "Jiyan": [
            weapon("Training Broadblade", "Broadblade", 250.00, 11.47),
            weapon("Tyro Broadblade", "Broadblade", 275.00, 14.85),
            weapon("Guardian Broadblade", "Broadblade", 325.00, 24.30),
            weapon("Broadblade of Voyager", "Broadblade", 300.00, 0.00),
            weapon("Originite: Type I", "Broadblade", 325.00, 0.00),
            weapon("Broadblade of Night", "Broadblade", 325.00, 24.30),
            weapon("Autumntrace", "Broadblade", 387.50, 0.00),
            weapon("Helios Cleaver", "Broadblade", 412.50, 30.38),
            weapon("Dauntless Evernight", "Broadblade", 337.50, 0.00),
            weapon("Broadblade#41", "Broadblade", 412.50, 0.00),
            weapon("Discord", "Broadblade", 337.50, 0.00),
            weapon("Lustrous Razor", "Broadblade", 587.50, 36.45),
            weapon("Verdant Summit", "Broadblade", 587.50, 0.00),
        ],
        "Yinlin": [
            weapon("Training Rectifier", "Rectifier", 250.00, 11.47),
            weapon("Tyro Rectifier", "Rectifier", 275.00, 14.85),
            weapon("Guardian Rectifier", "Rectifier", 325.00, 24.30),
            weapon("Rectifier of Voyager", "Rectifier", 300.00, 0.00),
            weapon("Originite: Type V", "Rectifier", 300.00, 0.00),
            weapon("Rectifier of Night", "Rectifier", 325.00, 24.30),
            weapon("Augment", "Rectifier", 412.50, 0.00),
            weapon("Comet Flare", "Rectifier", 412.50, 0.00),
            weapon("Jinzhou Keeper", "Rectifier", 387.50, 36.45),
            weapon("Rectifier#25", "Rectifier", 337.50, 0.00),
            weapon("Variation", "Rectifier", 337.50, 0.00),
            weapon("Cosmic Ripples", "Rectifier", 500.00, 54.00),
            weapon("Stringmaster", "Rectifier", 500.00, 0.0),
        ],
    }

    # Display character options
    print("Select a character:")
    for i, char in enumerate(characters):
        print(
            f"{i + 1}. {char.CharName} (Level: {char.CLevel}, HP: {char.CHP}, ATK: {char.CATK}, DEF: {char.CDEF}, Crit Rate: {char.CCRate}%, Crit Damage: {char.CCDMG}%)"
        )

    char_choice = (
        int(input("Enter the number of the character you want to select: ")) - 1
    )
    selected_char = characters[char_choice]
    my_build.add_character(selected_char)
    my_build.display_character()

    # Display weapon options
    print("Select a weapon:")
    available_weapons = weapons[selected_char.CharName]
    for i, weap in enumerate(available_weapons):
        print(
            f"{i + 1}. {weap.WName} (Type: {weap.WType}, Flat ATK: {weap.WFlatATK}, ATK Bonus: {weap.WATKBonus}%)"
        )

    weap_choice = int(input("Enter the number of the weapon you want to select: ")) - 1
    selected_weap = available_weapons[weap_choice]
    my_build.add_weapon(selected_weap)
    my_build.display_weapon()

    Base_Flat_Damage = selected_char.CATK + selected_weap.WFlatATK
    Base_Flat_Bonus = 0.00
    Base_Attack_Bonus = 1 + (selected_weap.WATKBonus / 100)
    Base_Attack = Base_Flat_Damage * Base_Attack_Bonus

    Crit_Rate = selected_char.CCRate
    Crit_Damage = selected_char.CCDMG

    print("Basic Attack - Vibration Manifestation:")
    Basic_Attack_P1 = Base_Attack * (59.15 / 100)
    Basic_Attack_P1_Crit = Basic_Attack_P1 * (Crit_Damage / 100)
    print(f"Part 1 damage: {Basic_Attack_P1:.2f}")
    print(f"Part 1 crit damage: {Basic_Attack_P1_Crit:.2f}")
    print(" ")
    Basic_Attack_P2 = Base_Attack * (76.05 / 100)
    Basic_Attack_P2_Crit = Basic_Attack_P2 * (Crit_Damage / 100)
    print(f"Part 2 damage: {Basic_Attack_P2:.2f}")
    print(f"Part 2 crit damage: {Basic_Attack_P2_Crit:.2f}")
    print(" ")
    Basic_Attack_P3 = Base_Attack * ((15.21 / 100) * 5)
    Basic_Attack_P3_Crit = Basic_Attack_P3 * (Crit_Damage / 100)
    print(f"Part 3 damage: {Basic_Attack_P3:.2f}")
    print(f"Part 3 crit damage: {Basic_Attack_P3_Crit:.2f}")
    print(" ")
    Basic_Attack_P4 = Base_Attack * (130.13 / 100)
    Basic_Attack_P4_Crit = Basic_Attack_P4 * (Crit_Damage / 100)
    print(f"Part 4 damage: {Basic_Attack_P4:.2f}")
    print(f"Part 4 crit damage: {Basic_Attack_P4_Crit:.2f}")
    print(" ")
    Heavy_Attack = Base_Attack * ((19.27 / 100) * 5)
    Heavy_Attack_Crit = Heavy_Attack * (Crit_Damage / 100)
    print(f"Heavy attack damage: {Heavy_Attack:.2f}")
    print(f"Heavy attack crit damage: {Heavy_Attack_Crit:.2f}")
    print(" ")
    Dodge_Counter = Base_Attack * (195.34 / 100)
    Dodge_Counter_Crit = Dodge_Counter * (Crit_Damage / 100)
    print(f"Dodge counter damage: {Dodge_Counter:.2f}")
    print(f"Dodge counter crit damage: {Dodge_Counter_Crit:.2f}")
    print(" ")
    HA_Resonance = Base_Attack * (76.058 / 100)
    HA_Resonance_Crit = HA_Resonance * (Crit_Damage / 100)
    print(f"HA Resonance damage: {HA_Resonance:.2f}")
    print(f"HA Resonance crit damage: {HA_Resonance_Crit:.2f}")
    print(" ")
    HA_Aftertune = Base_Attack * (126.75 / 100)
    HA_Aftertune_Crit = HA_Aftertune * (Crit_Damage / 100)
    print(f"HA Aftertune damage: {HA_Aftertune:.2f}")
    print(f"HA Aftertune crit damage: {HA_Aftertune_Crit:.2f}")
    print(" ")
    MidAir_Attack = Base_Attack * (104.78 / 100)
    MidAir_Attack_Crit = MidAir_Attack * (Crit_Damage / 100)
    print(f"MidAir attack damage: {MidAir_Attack:.2f}")
    print(f"MidAir attack crit damage: {MidAir_Attack_Crit:.2f}")
    print("---------------------------")

    print("Resonance Skill - Resonating Slashes:")
    Resonance_Skill = Base_Attack * (236.19 / 100)
    Resonance_Skill_Crit = Resonance_Skill * (Crit_Damage / 100)
    print(f"Resonance Skill damage: {Resonance_Skill:.2f}")
    print(f"Resonance Skill crit damage: {Resonance_Skill_Crit:.2f}")
    print("---------------------------")

    print("Resonance Liberation - Echoing Orchestra:")
    Resonance_Liberation_H1 = Base_Attack * (198.81 / 100)
    Resonance_Liberation_H1_Crit = Resonance_Liberation_H1 * (Crit_Damage / 100)
    print(f"H1 damage: {Resonance_Liberation_H1:.2f}")
    print(f"H1 crit damage: {Resonance_Liberation_H1_Crit:.2f}")
    print(" ")
    Resonance_Liberation_H2 = Base_Attack * (675.96 / 100)
    Resonance_Liberation_H2_Crit = Resonance_Liberation_H2 * (Crit_Damage / 100)
    print(f"H2 damage: {Resonance_Liberation_H2:.2f}")
    print(f"H2 crit damage: {Resonance_Liberation_H2_Crit:.2f}")
    print("---------------------------")

    print("Intro Skill - Waveshock:")
    Intro_Skill = Base_Attack * (168.99 / 100)
    Intro_Skill_Crit = Intro_Skill * (Crit_Damage / 100)
    print(f"Intro Skill damage: {Intro_Skill:.2f}")
    print(f"Intro Skill crit damage: {Intro_Skill_Crit:.2f}")
    print("---------------------------")

    print("Forte Circuit - World in a Grain of Sand:")
    Resonating_Spin = Base_Attack * ((129.08 / 100) * 2)
    Resonating_Spin_Crit = Resonating_Spin * (Crit_Damage / 100)
    print(f"Resonating Spin damage: {Resonating_Spin:.2f}")
    print(f"Resonating Spin crit damage: {Resonating_Spin_Crit:.2f}")
    print(" ")
    Resonance_Whirl = Base_Attack * (39.77 / 100)
    Resonance_Whirl_Crit = Resonance_Whirl * (Crit_Damage / 100)
    print(f"Resonance Whirl damage: {Resonance_Whirl:.2f}")
    print(f"Resonance Whirl crit damage: {Resonance_Whirl_Crit:.2f}")
    print(" ")
    Resonating_Echoes_P1 = Base_Attack * (79.53 / 100)
    Resonating_Echoes_P1_Crit = Resonating_Echoes_P1 * (Crit_Damage / 100)
    print(f"Resonating Echoes P1 damage: {Resonating_Echoes_P1:.2f}")
    print(f"Resonating Echoes P1 crit damage: {Resonating_Echoes_P1_Crit:.2f}")
    print(" ")
    Resonating_Echoes_P2 = Base_Attack * (159.05 / 100)
    Resonating_Echoes_P2_Crit = Resonating_Echoes_P2 * (Crit_Damage / 100)
    print(f"Resonating Echoes P2 damage: {Resonating_Echoes_P2:.2f}")
    print(f"Resonating Echoes P2 crit damage: {Resonating_Echoes_P2_Crit:.2f}")
    print("---------------------------")


main()
