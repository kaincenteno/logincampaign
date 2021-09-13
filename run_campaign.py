#!/bin/python3
import campaign_data

# Enter below the root folder of your game server and the month and year of the campaign to import.
GAME_FOLDER = ""
CAMPAIGN_MONTH = ""
CAMPAIGN_YEAR = ""

campaign_data.create_file(GAME_FOLDER, CAMPAIGN_MONTH, GAME_FOLDER)
