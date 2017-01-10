"""
This module will take care for saving a character to the database
"""
import sqlite3

from database.database_info import \
    (DB_PATH,
     DBINDEX_SAVED_CHARACTER_LOADED_SCRIPTS_TABLE_ID, DBINDEX_SAVED_CHARACTER_KILLED_MONSTERS_ID,
     DBINDEX_SAVED_CHARACTER_COMPLETED_QUESTS_ID, DBINDEX_SAVED_CHARACTER_INVENTORY_ID,
     DBINDEX_SAVED_CHARACTER_EQUIPMENT_ID,

     DB_SAVED_CHARACTER_TABLE_NAME,
     DB_SC_LOADED_SCRIPTS_TABLE_NAME, DB_SC_KILLED_MONSTERS_TABLE_NAME, DB_SC_EQUIPMENT_TABLE_NAME,
     DB_SC_COMPLETED_QUESTS_TABLE_NAME, DB_SC_INVENTORY_TABLE_NAME)
from entities import (Character, CHARACTER_EQUIPMENT_BELT_KEY, CHARACTER_EQUIPMENT_BOOTS_KEY,
                      CHARACTER_EQUIPMENT_CHESTGUARD_KEY, CHARACTER_EQUIPMENT_SHOULDERPAD_KEY,
                      CHARACTER_EQUIPMENT_HEADPIECE_KEY, CHARACTER_EQUIPMENT_NECKLACE_KEY,
                      CHARACTER_EQUIPMENT_BRACER_KEY, CHARACTER_EQUIPMENT_GLOVES_KEY, CHARACTER_EQUIPMENT_LEGGINGS_KEY)
from items import Item

ALLOWED_TABLES_TO_DELETE_FROM = ['saved_character_completed_quests', 'saved_character_inventory',
                                 'saved_character_killed_monsters', 'saved_character_loaded_scripts',
                                 'saved_character_equipment', 'saved_character']


def save_character(character: Character):
    """
    Save the character into the database
    """

    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()

        character_info = cursor.execute("SELECT * FROM saved_character WHERE name = ?", [character.name]).fetchone()

        character_level = character.level  # type: int
        character_class = character.get_class()  # type: str
        character_gold = character.inventory['gold']  # type: int

        # see if the character already has it's row (has been saved)
        if character_info:
            # we have saved this character before, therefore we have the table IDs
            character_loaded_scripts_id = character_info[DBINDEX_SAVED_CHARACTER_LOADED_SCRIPTS_TABLE_ID]
            character_killed_monsters_id = character_info[DBINDEX_SAVED_CHARACTER_KILLED_MONSTERS_ID]
            character_completed_quests_id = character_info[DBINDEX_SAVED_CHARACTER_COMPLETED_QUESTS_ID]
            character_inventory_id = character_info[DBINDEX_SAVED_CHARACTER_INVENTORY_ID]
            character_equipment_id = character_info[DBINDEX_SAVED_CHARACTER_EQUIPMENT_ID]
            cursor.execute(f'DELETE FROM {DB_SAVED_CHARACTER_TABLE_NAME} WHERE name = ?', [character.name])
        else:
            # we have not saved this character before, therefore we need to generate new IDs for the other tables
            character_loaded_scripts_id = get_highest_free_id_from_table(DB_SC_LOADED_SCRIPTS_TABLE_NAME, cursor)
            character_killed_monsters_id = get_highest_free_id_from_table(DB_SC_KILLED_MONSTERS_TABLE_NAME, cursor)
            character_completed_quests_id = get_highest_free_id_from_table(DB_SC_COMPLETED_QUESTS_TABLE_NAME, cursor)
            character_inventory_id = get_highest_free_id_from_table(DB_SC_INVENTORY_TABLE_NAME, cursor)
            character_equipment_id = get_highest_free_id_from_table(DB_SC_EQUIPMENT_TABLE_NAME, cursor)

        # save the main table
        cursor.execute('INSERT INTO saved_character VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       [character.name, character_class, character_level, character_loaded_scripts_id,
                        character_killed_monsters_id, character_completed_quests_id, character_equipment_id, character_inventory_id,
                        character_gold])

        # save the sub-tables
        save_loaded_scripts(character_loaded_scripts_id, character.loaded_scripts, cursor)
        save_killed_monsters(character_killed_monsters_id, character.killed_monsters, cursor)
        save_completed_quests(character_completed_quests_id, character.completed_quests, cursor)
        save_inventory(character_inventory_id, character.inventory, cursor)
        save_equipment(character_equipment_id, character.equipment, cursor)

        print("-" * 40)
        print(f'Character {character.name} was saved successfully!')
        print("-" * 40)


def save_loaded_scripts(id: int, loaded_scripts: set, cursor):
    """
    This function saves the character's loaded scripts into the saved_character_loaded_scripts DB table
    Table sample contents:
    id,    script_name
      1,     HASKELL_PRAXTON_CONVERSATION

    :param id: the ID we have to save as
    :param loaded_scripts: a set containing all the names -> {HASKEL_PRAXTON_CONVERSATION} in this case
    """

    delete_rows_from_table(table_name=DB_SC_LOADED_SCRIPTS_TABLE_NAME, id=id, cursor=cursor)  # delete the old values first

    for loaded_script in loaded_scripts:
        cursor.execute(f'INSERT INTO {DB_SC_LOADED_SCRIPTS_TABLE_NAME} VALUES (?, ?)', [id, loaded_script])


def save_killed_monsters(id: int, killed_monsters: set, cursor):
    """
    This function saves all the monsters that the character has killed into the saved_character_killed_monsters DB table
    Table sample contents:
    id,    GUID(of monster)
          1,     14
          1,      7
    IMPORTANT: This works only for monsters that by design should not be killed twice if the player restarts the game

    :param id:  the ID we have to save as
    :param killed_monsters: a set containing all the killed monster's GUIDs -> {14, 3, 2}
    """

    delete_rows_from_table(table_name=DB_SC_KILLED_MONSTERS_TABLE_NAME, id=id, cursor=cursor)  # delete the old values first

    for monster_guid in killed_monsters:
        cursor.execute(f'INSERT INTO {DB_SC_KILLED_MONSTERS_TABLE_NAME} VALUES (?, ?)', [id, monster_guid])


def save_completed_quests(id: int, completed_quests: set, cursor):
    """
    This function saves all the quests that the character has completed into the saved_character_completed_quests DB table
    Table sample contents:
    id,  quest_name
      1,   A Canine Menace
      1,   Canine-Like Hunger

    :param id: the ID we have to save as
    :param completed_quests: a set containing all the names of the completed quests -> {"A Canine Menace", "Canine-Like Hunger"} in this case
    """

    delete_rows_from_table(table_name=DB_SC_COMPLETED_QUESTS_TABLE_NAME, id=id, cursor=cursor)  # delete the old values first

    for quest_name in completed_quests:
        cursor.execute(f'INSERT INTO {DB_SC_COMPLETED_QUESTS_TABLE_NAME} VALUES (?, ?)', [id, quest_name])


def save_inventory(id: int, inventory: dict, cursor):
    """
    This function saves the character's inventory into the saved_character_inventory DB table
    Table sample contents:

        id, item_id, item_count
     1,       1,        5
     Meaning the character has 5 Wolf Meats in his inventory

    :param id: the ID we have to save as
    :param inventory: A dictionary, Key: item_name, Value: tuple(Item class instance, Item Count)
    """

    delete_rows_from_table(table_name=DB_SC_INVENTORY_TABLE_NAME, id=id, cursor=cursor)  # delete the old values first

    for item_name in inventory.keys():
        if item_name != 'gold':
            item_id = inventory[item_name][0].id  # get the instance of Item's ID
            item_count = inventory[item_name][1]

            cursor.execute(f'INSERT INTO {DB_SC_INVENTORY_TABLE_NAME} VALUES (?, ?, ?)', [id, item_id, item_count])


def save_equipment(id: int, equipment: dict, cursor):
    """
    This function saves the character's equipment into the saved_character_equipment DB table
    Table sample contents:

    id, headpiece_id, shoulderpad_id, necklace_id, chestguard_id, bracer_id, gloves_id, belt_id, leggings_id, boots_id
     1,           11,             12,        Null,            13,      Null,      Null,    Null,        Null,     Null
    :param id: the ID corresponding to the entry in saved_character_equipment
    :param equipment: the dictionary holding the equipped item for each character equipment slot
    """

    delete_rows_from_table(table_name=DB_SC_EQUIPMENT_TABLE_NAME, id=id, cursor=cursor)  # delete the old values first

    headpiece_id = get_item_id_or_none(equipment[CHARACTER_EQUIPMENT_HEADPIECE_KEY])
    shoulderpad_id = get_item_id_or_none(equipment[CHARACTER_EQUIPMENT_SHOULDERPAD_KEY])
    necklace_id = get_item_id_or_none(equipment[CHARACTER_EQUIPMENT_NECKLACE_KEY])
    chestguard_id = get_item_id_or_none(equipment[CHARACTER_EQUIPMENT_CHESTGUARD_KEY])
    bracer_id = get_item_id_or_none(equipment[CHARACTER_EQUIPMENT_BRACER_KEY])
    gloves_id = get_item_id_or_none(equipment[CHARACTER_EQUIPMENT_GLOVES_KEY])
    belt_id = get_item_id_or_none(equipment[CHARACTER_EQUIPMENT_BELT_KEY])
    leggings_id = get_item_id_or_none(equipment[CHARACTER_EQUIPMENT_LEGGINGS_KEY])
    boots_id = get_item_id_or_none(equipment[CHARACTER_EQUIPMENT_BOOTS_KEY])

    cursor.execute(f'INSERT INTO {DB_SC_EQUIPMENT_TABLE_NAME} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   [id, headpiece_id,shoulderpad_id, necklace_id, chestguard_id, bracer_id, gloves_id, belt_id,
                    leggings_id, boots_id])


def delete_rows_from_table(table_name: str, id: int, cursor):
    """
    This function will delete every row in TABLE_NAME with an id of ID
    :param table_name: a string -> "saved_character_loaded_scripts" for example
    :param id:  the id of the rows we want to delete -> 1

    The function is used whenever we want to save new information. To save the new updated information, we have to
    delete the old one first.
    """
    if table_name in ALLOWED_TABLES_TO_DELETE_FROM:
        cursor.execute(f'DELETE FROM {table_name} WHERE id = ?', [id])
    else:
        raise Exception(f'You do not have permission to delete from the {table_name} table!')


def get_highest_free_id_from_table(table_name: str, cursor):
    """
    This function returns the highest free unique id from a table
    This ID is most likely used to insert a new row into it
    """
    cursor.execute(f'SELECT max(id) FROM {table_name}')
    max_id = cursor.fetchone()[0]

    return max_id + 1


def get_item_id_or_none(item):
    """
    This function returns the item_id of an item.
    We check if the item we're given is None. If it is None, we return None
    """
    if isinstance(item, Item):
        return item.id

    return None



