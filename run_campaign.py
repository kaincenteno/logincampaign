#!/bin/python3
import settings
import campaign_data


campaign_data.create_file(
    settings.CAMPAIGN_YEAR,
    settings.CAMPAIGN_MONTH,
    settings.GAME_FOLDER)
campaign_data.enable_login_campaign(settings.GAME_FOLDER)
campaign_data.change_campaign_date(
    settings.CAMPAIGN_YEAR,
    settings.CAMPAIGN_MONTH,
    settings.CAMPAIGN_DAY,
    settings.CAMPAIGN_DURATION,
    settings.GAME_FOLDER)
