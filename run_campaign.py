#!/bin/python3
from data import settings
from data import campaign_data

if settings.DOCKER:
    campaign_data.create_file(
        settings.DOCKER,
        settings.CAMPAIGN_NUMBER,
        settings.GAME_FOLDER)
else:
    campaign_data.create_file(
        settings.DOCKER,
        settings.CAMPAIGN_NUMBER,
        settings.GAME_FOLDER)
    campaign_data.create_file(
        settings.CAMPAIGN_NUMBER,
        settings.GAME_FOLDER)
    campaign_data.enable_login_campaign(settings.GAME_FOLDER)
    campaign_data.change_campaign_date(
        settings.CAMPAIGN_NUMBER,
        settings.CAMPAIGN_DAY,
        settings.CAMPAIGN_DURATION,
        settings.GAME_FOLDER)
