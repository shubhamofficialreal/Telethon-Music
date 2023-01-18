import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "27899654"))
    API_HASH = os.environ.get("API_HASH", "644a291c69677a2fd785c43455b1df08")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5921690368:AAH2ZYQyqkhrdwjxwWk_wnGaPV8wkooC30o")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BAANlTiEhDU9GMyvBOoWg8G4IKVhkXxzm2eY5mtKO3oJZFqIvpe_NZFo9L8AcrXnhKPZsfjrSIshvHTMpKs_okfEenYRaabiGJTQznmJfeirBiGw_7ApckGUdNWzm48XlZfVlIgt3irtRRQNGfJXwSt3bPYkzKmAcZD2F_pVSJrssPSm_uHWudOlVj58r9QjquMzc9k9vYcv94IM__c7MxzHW10oPYC9JZmTGWm35cDEv5l2dNT2_JP9s3Js-8pUrO6tuWtnyqrkwcSPudbQej8FAN109GxxccNmSfVi1dWgTAKIXiRXwXPZ5tGz3ip32YEwPg5FQUzs8qggzOUcBbrYAAAAAUIqpGoA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MeTimeXUnlimitedME_Bot")
    SUPPORT = os.environ.get("SUPPORT", "blazerocks") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "me_time_for_uh") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/17dbc30e1c8e6480d76f9.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/2183e7a2a308e46dd2d55.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5405058154")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "1000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
