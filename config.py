import os

API_ID = os.environ.get("API_ID", "28235190")

API_HASH = os.environ.get("API_HASH", "a685e1bccefafc462baf123cff9a1be3")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7671032055:AAFbf4U7oWa2mrt4IyJ6FwPazgBvJSyP1YY")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7944235618))

LOG = -1002219766314,

 UPDATE_GRP = -1002560485204, # bot sat group

 auth_chats = [7944235618]

try:
    ADMINS=[7944235618]
    for x in (os.environ.get("ADMINS", "7944235618").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
