import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6540119363:AAHrjL7BwstvByKGc-ERHxJWD5DaBzGkhao")

    APP_ID = int(os.environ.get("APP_ID", 6379161238))

    API_HASH = os.environ.get("API_HASH", "fe77fbf0cae9f7f5ece37659e2466cf1")
