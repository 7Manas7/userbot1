# COPYRIGHT (C) 2021 BY 7manas7
"""
"""
# MADE BY 7manas7 🔥
# MY IDEA H YRR DONT KANG THIS PLEASE
import asyncio
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
try:
  from 7manas7 import devs, id, ID, 7manas7
except:
  os.system("pip install 7manas7")
try:
  from ULTRA import bot 
except:
  pass
from LEGENDX import devs, id, ID
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("legend", API_ID, API_HASH).start(bot_token=token)
import time
botnickname = os.environ.get("BOT_NICK_NAME")
ALIVE_NAME = os.environ.get("ALIVE_NAME")
BOT = str(botnickname) if botnickname else "userbot1"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "userbot1"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
MASTERBOT = "[userbot1 team](https://t.me/teamuserbot1)"
VERSION = "0.0.1"
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)
ALIVE_BOT_USERNAME = os.environ.get("ALIVE_BOT_USERNAME", None)
devs = devs
ID = ID
id = id
REPO = "[υserbot1 вσт](https://github.com/7manas7/userbot1)"

MASTER = NAME
GROUP = "[UPDATES CHANNEL](https://t.me/userbot1updates)"
if __name__=="__main__":
  bot.start()
  bot.run_until_disconnected()
  xbot.run_until_disconnected()
