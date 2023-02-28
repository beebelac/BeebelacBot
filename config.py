import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1622957309").split()))
OWNER_ID = int(getenv("OWNER_ID, "1622957309")) #ur id
MONGO_URL = getenv("MONGO_URL, "mongodb+srv://beebelacaja:beebelac@beebelac.bvkxulj.mongodb.net/?retryWrites=true&w=majority") # an database
BOT_TOKEN = getenv("BOT_TOKEN", "6264816249:AAE6zBHIZzLC_YaccwpFeAdZT7QaCZPzPcY")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT") #optional
PM_LOGGER = getenv("PM_LOGGER") # I'd if uh want
LOG_GROUP = getenv("LOG_GROUP") #id if uh want to enable tagalert
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAB3zSpvPQngarGV5-i3KiZsXk-3Kt5y6d-YfUR2EmdOYKad65BZ7ehNhbLzO8dULKuVSYYK5v8_C29dOX3SFBgsqU8r47EwhngoCi6xZWHbqgkFP4wwez97mypbUEO7-BYvmxLrS6eV84YgMcrkdIUyD4raJzlGpq5eVu4iGyyJrSDmJWURZB4-TkTU3l06x3s6umC3TGpGqii_kwC70uvSW8MowmmINeQn_LuGCGCCUy69KYIds8bj_ePcnGK4Mi1SUi-lwEdQc4pCMLhDWsY376MRXwuM-IPDsEw6lemSdIFMUFQDWHx6eSY4VXDldxEbMCFk65wwrEqdyQLDU3pgAAAABgvFz9AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
