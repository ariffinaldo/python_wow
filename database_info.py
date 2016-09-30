"""
This module holds all kinds of information regarding the database and it's tables.
"""
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.join(DIR_PATH, "python_wowDB.db")

"""
The table indexes will be defined below this comment. They are:
The number that is associated with the table's column if all the columns are taken
Example: Table has columns X, Y, Z
X would be column number 0
Y - 1
Z - 2
"""

# saved_character table
DB_SAVED_CHARACTER_TABLE_NAME = 'saved_character'
DBINDEX_SAVED_CHARACTER_NAME = 0
DBINDEX_SAVED_CHARACTER_CLASS = 1
DBINDEX_SAVED_CHARACTER_LEVEL = 2
DBINDEX_SAVED_CHARACTER_LOADED_SCRIPTS_TABLE_ID = 3
DBINDEX_SAVED_CHARACTER_KILLED_MONSTERS_ID = 4
DBINDEX_SAVED_CHARACTER_COMPLETED_QUESTS_ID = 5
DBINDEX_SAVED_CHARACTER_INVENTORY_ID = 6
DBINDEX_SAVED_CHARACTER_GOLD = 7

# saved_character_loaded_scripts
DB_LOADED_SCRIPTS_TABLE_NAME = 'saved_character_loaded_scripts'
DBINDEX_SC_LOADED_SCRIPTS_ID = 0
DBINDEX_SC_LOADED_SCRIPTS_SCRIPT_NAME = 1

# saved_character_killed_monsters table
DB_KILLED_MONSTERS_TABLE_NAME = 'saved_character_killed_monsters'
DBINDEX_SC_KILLED_MONSTERS_ID = 0
DBINDEX_SC_KILLED_MONSTERS_GUID = 1

# saved_character_inventory
DB_INVENTORY_TABLE_NAME = 'saved_character_inventory'
DBINDEX_SC_INVENTORY_ID = 0
DBINDEX_SC_INVENTORY_ITEM_ID = 1
DBINDEX_SC_INVENTORY_ITEM_COUNT = 2

# saved_character_completed_quests table
DB_COMPLETED_QUESTS_TABLE_NAME = 'saved_character_completed_quests'
DBINDEX_SC_COMPLETED_QUESTS_ID = 0
DBINDEX_SC_COMPLETED_QUESTS_NAME = 1

# creature_default_armor table
DBINDEX_CREATURE_DEFAULT_ARMOR_LEVEL = 0
DBINDEX_CREATURE_DEFAULT_ARMOR_ARMOR = 1

# creature_default_xp_rewards table
DBINDEX_CREATURE_DEFAULT_XP_REWARDS_ENTRY = 0
DBINDEX_CREATURE_DEFAULT_XP_REWARDS_LEVEL = 1
DBINDEX_CREATURE_DEFAULT_XP_REWARDS_XP = 2

# creature_default_gold_rewards table
DBINDEX_CREATURE_DEFAULT_GOLD_REWARDS_LEVEL = 0
DBINDEX_CREATURE_DEFAULT_GOLD_REWARDS_MIN_GOLD_REWARD = 1
DBINDEX_CREATURE_DEFAULT_GOLD_REWARDS_MAX_GOLD_REWARD = 2

# creature_template table
DBINDEX_CREATURE_TEMPLATE_ENTRY = 0
DBINDEX_CREATURE_TEMPLATE_NAME = 1
DBINDEX_CREATURE_TEMPLATE_TYPE = 2
DBINDEX_CREATURE_TEMPLATE_LEVEL = 3
DBINDEX_CREATURE_TEMPLATE_HEALTH = 4
DBINDEX_CREATURE_TEMPLATE_MANA = 5
DBINDEX_CREATURE_TEMPLATE_ARMOR = 6
DBINDEX_CREATURE_TEMPLATE_MIN_DMG = 7
DBINDEX_CREATURE_TEMPLATE_MAX_DMG = 8
DBINDEX_CREATURE_TEMPLATE_QUEST_RELATION_ID = 9
DBINDEX_CREATURE_TEMPLATE_LOOT_TABLE_ID = 10
DBINDEX_CREATURE_TEMPLATE_GOSSIP = 11
DBINDEX_CREATURE_TEMPLATE_RESPAWNABLE = 12

# creatures table
DBINDEX_CREATURES_GUID = 0
DBINDEX_CREATURES_CREATURE_ID = 1
DBINDEX_CREATURES_TYPE = 2
DBINDEX_CREATURES_ZONE = 3
DBINDEX_CREATURES_SUB_ZONE = 4

# npc_vendor template
DBINDEX_NPC_VENDOR_CREATURE_ENTRY = 0
DBINDEX_NPC_VENDOR_ITEM_ID = 1
DBINDEX_NPC_VENDOR_ITEM_COUNT = 2
DBINDEX_NPC_VENDOR_PRICE = 3

# item_template table
DBINDEX_ITEM_TEMPLATE_ENTRY = 0
DBINDEX_ITEM_TEMPLATE_NAME = 1
DBINDEX_ITEM_TEMPLATE_TYPE = 2
DBINDEX_ITEM_TEMPLATE_BUY_PRICE = 3
DBINDEX_ITEM_TEMPLATE_SELL_PRICE = 4
DBINDEX_ITEM_TEMPLATE_MIN_DMG = 5
DBINDEX_ITEM_TEMPLATE_MAX_DMG = 6
DBINDEX_ITEM_TEMPLATE_QUEST_ID = 7
DBINDEX_ITEM_TEMPLATE_EFFECT = 8

# level_xp_requirement table
DBINDEX_LEVEL_XP_REQUIREMENT_LEVEL = 0
DBINDEX_LEVEL_XP_REQUIREMENT_XP_REQUIRED = 1

# levelup_stats table
DBINDEX_LEVELUP_STATS_LEVEL = 0
DBINDEX_LEVELUP_STATS_HEALTH = 1
DBINDEX_LEVELUP_STATS_MANA = 2
DBINDEX_LEVELUP_STATS_STRENGTH = 3
DBINDEX_LEVELUP_STATS_AGILITY = 4
DBINDEX_LEVELUP_STATS_ARMOR = 5

# spell_buffs table
DBINDEX_SPELL_BUFFS_ENTRY = 0
DBINDEX_SPELL_BUFFS_NAME = 1
DBINDEX_SPELL_BUFFS_DURATION = 2
DBINDEX_SPELL_BUFFS_STAT1 = 3
DBINDEX_SPELL_BUFFS_AMOUNT1 = 4
DBINDEX_SPELL_BUFFS_STAT2 = 5
DBINDEX_SPELL_BUFFS_AMOUNT2 = 6
DBINDEX_SPELL_BUFFS_STAT3 = 7
DBINDEX_SPELL_BUFFS_AMOUNT3 = 8
DBINDEX_SPELL_BUFFS_COMMENT = 9

# spell_dots table
DBINDEX_SPELL_DOTS_ENTRY = 0
DBINDEX_SPELL_DOTS_NAME = 1
DBINDEX_SPELL_DOTS_DAMAGE_PER_TICK = 2
DBINDEX_SPELL_DOTS_DAMAGE_SCHOOL = 3
DBINDEX_SPELL_DOTS_DURATION = 4
DBINDEX_SPELL_DOTS_COMMENT = 5

# paladin_spells_template table
DBINDEX_PALADIN_SPELLS_TEMPLATE_ID = 0
DBINDEX_PALADIN_SPELLS_TEMPLATE_NAME = 1
DBINDEX_PALADIN_SPELLS_TEMPLATE_RANK = 2
DBINDEX_PALADIN_SPELLS_TEMPLATE_LEVEL_REQUIRED = 3
DBINDEX_PALADIN_SPELLS_TEMPLATE_DAMAGE1 = 4
DBINDEX_PALADIN_SPELLS_TEMPLATE_DAMAGE2 = 5
DBINDEX_PALADIN_SPELLS_TEMPLATE_DAMAGE3 = 6
DBINDEX_PALADIN_SPELLS_TEMPLATE_HEAL1 = 7
DBINDEX_PALADIN_SPELLS_TEMPLATE_HEAL2 = 8
DBINDEX_PALADIN_SPELLS_TEMPLATE_HEAL3 = 9
DBINDEX_PALADIN_SPELLS_TEMPLATE_MANA_COST = 10
DBINDEX_PALADIN_SPELLS_TEMPLATE_EFFECT = 11
DBINDEX_PALADIN_SPELLS_TEMPLATE_COOLDOWN = 12
DBINDEX_PALADIN_SPELLS_TEMPLATE_COMMENT = 13

# quest_template table
DBINDEX_QUEST_TEMPLATE_ENTRY = 0
DBINDEX_QUEST_TEMPLATE_NAME = 1
DBINDEX_QUEST_TEMPLATE_TYPE = 2
DBINDEX_QUEST_TEMPLATE_LEVEL_REQUIRED = 3
DBINDEX_QUEST_TEMPLATE_MONSTER_REQUIRED = 4
DBINDEX_QUEST_TEMPLATE_ITEM_REQUIRED = 5
DBINDEX_QUEST_TEMPLATE_AMOUNT_REQUIRED = 6
DBINDEX_QUEST_TEMPLATE_ZONE = 7
DBINDEX_QUEST_TEMPLATE_SUB_ZONE = 8
DBINDEX_QUEST_TEMPLATE_XP_REWARD = 9
DBINDEX_QUEST_TEMPLATE_COMMENT = 10
DBINDEX_QUEST_TEMPLATE_ITEM_REWARD1 = 11
DBINDEX_QUEST_TEMPLATE_ITEM_REWARD2 = 12
DBINDEX_QUEST_TEMPLATE_ITEM_REWARD3 = 13
DBINDEX_QUEST_TEMPLATE_ITEM_CHOICE_ENABLED = 14
