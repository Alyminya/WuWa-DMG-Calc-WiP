from Characters import character
from Weapons import weapon

class Build():
    def __init__(self):
        self.build = []
    
    def add_character(self, built_character):
        self.build.append(built_character)

    def add_weapon(self, built_weapon):
        self.build.append(built_weapon)
    
    def display_character(self):
         print('Current character:')
         for c in self.build:
            print('Character: ', c.CharName)
            print('Level: ', c.CLevel)
            print('HP: ', c.CHP)
            print('ATK: ', c.CATK)
            print('DEF: ', c.CDEF)
            print(f'Crit Rate:  {c.CCRate:.1f}%')
            print(f'Crit Damage:  {c.CCDMG:.1f}%')
            print('----------------------------')

    def display_weapon(self):
        print('Current weapon:')
        for w in self.build:
            if isinstance(w, weapon):
                print('Weapon: ', w.WName)
                print('Type: ', w.WType)
                print('Flat ATK: ', w.WFlatATK)
                print(f'ATK Bonus: {w.WATKBonus:.1f}%')
                print('----------------------------')
        
def main():
    my_build = Build()
    
    SRover = character("Spectro Rover", 90, 1144.00, 375.00, 1368.00, 5.00, 150.00)
    my_build.add_character(SRover)
    my_build.display_character()
    
    Sword18 = weapon("Sword#18", "Sword", 387.00, 36.4)
    my_build.add_weapon(Sword18)
    my_build.display_weapon()
   
    Base_Flat_Damage = SRover.CATK + Sword18.WFlatATK
    Base_Flat_Bonus = 0.00
    Base_Attack_Bonus = 1 + (Sword18.WATKBonus / 100)
    Base_Attack = Base_Flat_Damage * Base_Attack_Bonus

    Crit_Rate = SRover.CCRate
    Crit_Damage = SRover.CCDMG

    print('Basic Attack - Vibration Manifestation:')
    Basic_Attack_P1 = Base_Attack * (59.15 / 100)
    Basic_Attack_P1_Crit = Basic_Attack_P1 * (Crit_Damage / 100)
    print(f'Part 1 damage: {Basic_Attack_P1:.2f}')
    print(f'Part 1 crit damage: {Basic_Attack_P1_Crit:.2f}')
    print(' ')
    Basic_Attack_P2 = Base_Attack * (76.05 / 100)
    Basic_Attack_P2_Crit = Basic_Attack_P2 * (Crit_Damage / 100)
    print(f'Part 2 damage: {Basic_Attack_P2:.2f}')
    print(f'Part 2 crit damage: {Basic_Attack_P2_Crit:.2f}')
    print(' ')
    Basic_Attack_P3 = Base_Attack * ((15.21 / 100) * 5)
    Basic_Attack_P3_Crit = Basic_Attack_P3 * (Crit_Damage / 100)
    print(f'Part 3 damage: {Basic_Attack_P3:.2f}')
    print(f'Part 3 crit damage: {Basic_Attack_P3_Crit:.2f}')
    print(' ')
    Basic_Attack_P4 = Base_Attack * (130.13 / 100)
    Basic_Attack_P4_Crit = Basic_Attack_P4 * (Crit_Damage / 100)
    print(f'Part 4 damage: {Basic_Attack_P4:.2f}')
    print(f'Part 4 crit damage: {Basic_Attack_P4_Crit:.2f}')
    print(' ')
    Heavy_Attack = Base_Attack * ((19.27 / 100) * 5)
    Heavy_Attack_Crit = Heavy_Attack * (Crit_Damage / 100)
    print(f'Heavy attack damage: {Heavy_Attack:.2f}')
    print(f'Heavy attack crit damage: {Heavy_Attack_Crit:.2f}')
    print(' ')
    Dodge_Counter = Base_Attack * (195.34 / 100)
    Dodge_Counter_Crit = Dodge_Counter * (Crit_Damage / 100)
    print(f'Dodge counter damage: {Dodge_Counter:.2f}')
    print(f'Dodge counter crit damage: {Dodge_Counter_Crit:.2f}')
    print(' ')
    HA_Resonance = Base_Attack * (76.058 / 100)
    HA_Resonance_Crit = HA_Resonance * (Crit_Damage / 100)
    print(f'HA Resonance damage: {HA_Resonance:.2f}')
    print(f'HA Resonance crit damage: {HA_Resonance_Crit:.2f}')
    print(' ')
    HA_Aftertune = Base_Attack * (126.75 / 100)
    HA_Aftertune_Crit = HA_Aftertune * (Crit_Damage / 100)
    print(f'HA Aftertune damage: {HA_Aftertune:.2f}')
    print(f'HA Aftertune crit damage: {HA_Aftertune_Crit:.2f}')
    print(' ')
    MidAir_Attack = Base_Attack * (104.78 / 100)
    MidAir_Attack_Crit = MidAir_Attack * (Crit_Damage / 100)
    print(f'MidAir attack damage: {MidAir_Attack:.2f}')
    print(f'MidAir attack crit damage: {MidAir_Attack_Crit:.2f}')
    print('---------------------------')

    print('Resonance Skill - Resonating Slashes:')
    Resonance_Skill = Base_Attack * (236.19 / 100)
    Resonance_Skill_Crit = Resonance_Skill * (Crit_Damage / 100)
    print(f'Resonance Skill damage: {Resonance_Skill:.2f}')
    print(f'Resonance Skill crit damage: {Resonance_Skill_Crit:.2f}')
    print('---------------------------')

    print('Resonance Liberation - Echoing Orchestra:')
    Resonance_Liberation_H1 = Base_Attack * (198.81 / 100)
    Resonance_Liberation_H1_Crit = Resonance_Liberation_H1 * (Crit_Damage / 100)
    print(f'H1 damage: {Resonance_Liberation_H1:.2f}')
    print(f'H1 crit damage: {Resonance_Liberation_H1_Crit:.2f}')
    print(' ')
    Resonance_Liberation_H2 = Base_Attack * (675.96 / 100)
    Resonance_Liberation_H2_Crit = Resonance_Liberation_H2 * (Crit_Damage / 100)
    print(f'H2 damage: {Resonance_Liberation_H2:.2f}')
    print(f'H2 crit damage: {Resonance_Liberation_H2_Crit:.2f}')
    print('---------------------------')

    print('Intro Skill - Waveshock:')
    Intro_Skill = Base_Attack * (168.99 / 100)
    Intro_Skill_Crit = Intro_Skill * (Crit_Damage / 100)
    print(f'Intro Skill damage: {Intro_Skill:.2f}')
    print(f'Intro Skill crit damage: {Intro_Skill_Crit:.2f}')
    print('---------------------------')

    print('Forte Circuit - World in a Grain of Sand:')
    Resonating_Spin = Base_Attack * ((129.08 / 100) * 2)
    Resonating_Spin_Crit = Resonating_Spin * (Crit_Damage / 100)
    print(f'Resonating Spin damage: {Resonating_Spin:.2f}')
    print(f'Resonating Spin crit damage: {Resonating_Spin_Crit:.2f}')
    print(' ')
    Resonance_Whirl = Base_Attack * (39.77 / 100)
    Resonance_Whirl_Crit = Resonance_Whirl * (Crit_Damage / 100)
    print(f'Resonance Whirl damage: {Resonance_Whirl:.2f}')
    print(f'Resonance Whirl crit damage: {Resonance_Whirl_Crit:.2f}')
    print(' ')
    Resonating_Echoes_P1 = Base_Attack * (79.53 / 100)
    Resonating_Echoes_P1_Crit = Resonating_Echoes_P1 * (Crit_Damage / 100)
    print(f'Resonating Echoes P1 damage: {Resonating_Echoes_P1:.2f}')
    print(f'Resonating Echoes P1 crit damage: {Resonating_Echoes_P1_Crit:.2f}')
    print(' ')
    Resonating_Echoes_P2 = Base_Attack * (159.05 / 100)
    Resonating_Echoes_P2_Crit = Resonating_Echoes_P2 * (Crit_Damage / 100)
    print(f'Resonating Echoes P2 damage: {Resonating_Echoes_P2:.2f}')
    print(f'Resonating Echoes P2 crit damage: {Resonating_Echoes_P2_Crit:.2f}')
    print('---------------------------')
    
main()
