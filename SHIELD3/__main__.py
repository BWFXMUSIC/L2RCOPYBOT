import asyncio
import importlib
from pyrogram import idle
from L2RCOPYBOT import L2RCOPYBOT
from L2RCOPYBOT.modules import ALL_MODULES

LOGGER_ID = -1002010924139

loop = asyncio.get_event_loop()

async def roy_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("L2RCOPYBOT.modules." + all_module)
    print("♥︎ B𝗈𝗍 Started Successfully.")
    await idle()
    print("♥︎ Don't edit baby, otherwise you get an error. @H_CC_HELP")
    await L2RCOPYBOT.send_message(LOGGER_ID, "**✦ ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ.\n\n✦ ᴊᴏɪɴ - @The_Friendz**")

if __name__ == "__main__":
    loop.run_until_complete(roy_bot())




