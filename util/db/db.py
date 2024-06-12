
import os.path
import json
from . import model
from typing import Any, Callable

DB_PATH = './data'
WEAPONS_DATA    = 'weapons.json'
CHARACTERS_DATA = 'characters.json'

SCHEMA_PATH = '_schemas'
WEAPONS_SCHEMA    = 'weapons.schema.json'
CHARACTERS_SCHEMA = 'characters.schema.json'
WEAPON_SCHEMA     = 'weapon.schema.json'
CHARACTER_SCHEMA  = 'character.schema.json'

fp_weapons_data    = os.path.join(DB_PATH, WEAPONS_DATA)
fp_characters_data = os.path.join(DB_PATH, CHARACTERS_DATA)

fp_weapon_schema     = os.path.join(DB_PATH, SCHEMA_PATH, WEAPON_SCHEMA)
fp_weapons_schema    = os.path.join(DB_PATH, SCHEMA_PATH, WEAPONS_SCHEMA)
fp_character_schema  = os.path.join(DB_PATH, SCHEMA_PATH, CHARACTER_SCHEMA)
fp_characters_schema = os.path.join(DB_PATH, SCHEMA_PATH, CHARACTERS_SCHEMA)

def load_validate_json(json_path: str, json_schema_path: str) -> dict[str, Any]:
    with open(json_path, mode='r') as data_file:
        data = json.load(data_file)
    return data

def opt_field[T,U](cls: Callable[[Any], T], data: dict[str, Any], key: str, default: U) -> T|U:
    # TODO(flysand): These should probably do run-time type checks as well
    # otherwise we're in for a lot of trouble. I'm not that experienced
    # in python to be able to do it correctly. Even figuring out the correct
    # signature for this function was a lot...
    return cls(data[key]) if key in data else default

def load_db() -> model.DB:
    db = model.DB()
    db.characters = {}
    characters_data = load_validate_json(fp_characters_data, fp_characters_schema)
    for character_id in characters_data:
        character_data = load_validate_json(os.path.join(DB_PATH, characters_data[character_id]), fp_character_schema)
        character = model.Character_Info()
        character.id = character_data['id']
        character.name = character_data['name']
        character.rarity = character_data['rarity']
        character.affiliation = character_data['affiliation']
        character.base_atk_scaling = character_data['stats']['atk']
        character.base_hp_scaling = character_data['stats']['hp']
        character.base_def_scaling = character_data['stats']['def']
        character.max_forte = character_data['max_forte']
        character.weapon = character_data['weapon']
        character.element = character_data['element']
        character.move_multipliers = character_data['moves']['multipliers']
        move_meta = character_data['moves']['meta']
        character.moves = {}
        for move_id in move_meta:
            meta = move_meta[move_id]
            move = model.Move()
            move.id = move_id
            move.name = meta['name']
            move.forte_type = meta['forte_type']
            move.move_type = meta['move_type']
            move.strikes = meta['strikes']
            move.after = meta['after']
            move.chain = opt_field(str, meta, 'chain', None)
            move.fe_req = opt_field(int, meta, 'fe_req', None)
            move.fe_yield = opt_field(int, meta, 'fe_yield', None)
            move.sta_req = opt_field(int, meta, 'stamina', None) # TODO(flysand): rename the field
            move.con_yield = opt_field(int, meta, 'con_yield', None)
            character.moves[move_id] = move
        db.characters[character.id] = character
    db.weapons = {}
    weapons_data = load_validate_json(fp_weapons_data, fp_weapons_schema)
    for weapon_id in weapons_data:
        weapon_data = load_validate_json(os.path.join(DB_PATH, weapons_data[weapon_id]), fp_weapon_schema)
        weapon = model.Weapon_Info()
        weapon.id = weapon_data['id']
        weapon.name = weapon_data['name']
        weapon.rarity = weapon_data['rarity']
        weapon.type = weapon_data['weapon_type']
        weapon.atk_scaling = weapon_data['atk']
        weapon.sub_scaling = weapon_data['substat']['scaling']
        weapon.sub_stat = weapon_data['substat']['type']
        db.weapons[weapon.id] = weapon
    return db

data = load_db()
