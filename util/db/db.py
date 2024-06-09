
import os.path
import json
from . import model
import jsonschema
from typing import Any, Type, Callable

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

def load_validate_json(json_path: str, json_schema_path: str):
    with open(json_path, mode='r') as data_file:
        data = json.load(data_file)
    with open(json_schema_path, mode='r') as schema_file:
        schema = json.load(schema_file)
    jsonschema.validate(data, schema)
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
        character.forte_multipliers = character_data['attacks']['multipliers']
        forte_meta = character_data['attacks']['meta']
        character.fortes = {}
        for forte_id in forte_meta:
            meta = forte_meta[forte_id]
            forte = model.Forte()
            forte.id = forte_id
            forte.skill     = meta['skill']
            forte.strikes   = meta['strikes']
            forte.after     = meta['after']
            forte.chain     = opt_field(str, meta, 'chain', None)
            forte.fe_req    = opt_field(int, meta, 'fe_req', None)
            forte.fe_yield  = opt_field(int, meta, 'fe_yield', None)
            forte.sta_req   = opt_field(int, meta, 'stamina', None) # TODO(flysand): rename the field
            forte.con_yield = opt_field(int, meta, 'con_yield', None)
            character.fortes[forte_id] = forte
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
