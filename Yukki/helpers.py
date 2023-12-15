#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiAFKBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiAFKBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio

from typing import Union
from datetime import datetime, timedelta
from Yukki import cleanmode, app, botname
from Yukki.database import is_cleanmode_on
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


async def put_cleanmode(chat_id, message_id):
    if chat_id not in cleanmode:
        cleanmode[chat_id] = []
    time_now = datetime.now()
    put = {
        "msg_id": message_id,
        "timer_after": time_now + timedelta(minutes=5),
    }
    cleanmode[chat_id].append(put)


async def auto_clean():
    while not await asyncio.sleep(30):
        try:
            for chat_id in cleanmode:
                if not await is_cleanmode_on(chat_id):
                    continue
                for x in cleanmode[chat_id]:
                    if datetime.now() > x["timer_after"]:
                        try:
                            await app.delete_messages(chat_id, x["msg_id"])
                        except FloodWait as e:
                            await asyncio.sleep(e.x)
                        except:
                            continue
                    else:
                        continue
        except:
            continue


asyncio.create_task(auto_clean())


RANDOM = [
    "https://telegra.ph/file/5ea1fedb75d48a8f23136.jpg",
    "https://telegra.ph/file/7639930f1cdf333e4b583.jpg",
    "https://telegra.ph/file/24bf4591b3714e0a0ab8e.jpg",
    "https://telegra.ph/file/a9af59d751e1b1db8cbbd.jpg",
    "https://telegra.ph/file/903329e79d0efba915d0f.jpg",
    "https://telegra.ph/file/b7c64448a0ecc59e5312e.jpg",
    "https://telegra.ph/file/66e806967268954a81dfe.jpg",
    "https://telegra.ph/file/daf6557d448b528611fea.jpg",
    "https://telegra.ph/file/f542cc310004d96fd241e.jpg",
    "https://telegra.ph/file/09b2df10aea6a797a2e78.jpg",
    "https://telegra.ph/file/fb25f957d4ad66bdbffab.jpg"
]


HELP_TEXT = f"""ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {botname}'ꜱ ʜᴇʟᴘ ꜱᴇᴄᴛɪᴏɴ.

- ᴡʜᴇɴ ꜱᴏᴍᴇᴏɴᴇ ᴍᴇɴᴛɪᴏɴꜱ ʏᴏᴜ ɪɴ ᴀ ᴄʜᴀᴛ, ᴛʜᴇ ᴜꜱᴇʀ ᴡɪʟʟ ʙᴇ ɴᴏᴛɪꜰɪᴇᴅ ʏᴏᴜ ᴀʀᴇ ᴀꜰᴋ. ʏᴏᴜ ᴄᴀɴ ᴇᴠᴇɴ ᴘʀᴏᴠɪᴅᴇ ᴀ ʀᴇᴀꜱᴏɴ ꜰᴏʀ ɢᴏɪɴɢ ᴀꜰᴋ, ᴡʜɪᴄʜ ᴡɪʟʟ ʙᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴜꜱᴇʀ ᴀꜱ ᴡᴇʟʟ.


/afk - ᴛʜɪꜱ ᴡɪʟʟ ꜱᴇᴛ ʏᴏᴜ ᴏꜰꜰʟɪɴᴇ.

/afk [ʀᴇᴀꜱᴏɴ] - ᴛʜɪꜱ ᴡɪʟʟ ꜱᴇᴛ ʏᴏᴜ ᴏꜰꜰʟɪɴᴇ ᴡɪᴛʜ ᴀ ʀᴇᴀꜱᴏɴ.

/afk [ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴀ ꜱᴛɪᴄᴋᴇʀ/ᴘʜᴏᴛᴏ] - ᴛʜɪꜱ ᴡɪʟʟ ꜱᴇᴛ ʏᴏᴜ ᴏꜰꜰʟɪɴᴇ ᴡɪᴛʜ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ ꜱᴛɪᴄᴋᴇʀ.

/afk [ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴀ ꜱᴛɪᴄᴋᴇʀ/ᴘʜᴏᴛᴏ] [ʀᴇᴀꜱᴏɴ] - ᴛʜɪꜱ ᴡɪʟʟ ꜱᴇᴛ ʏᴏᴜ ᴀꜰᴋ ᴡɪᴛʜ ᴀɴ ɪᴍᴀɢᴇ ᴀɴᴅ ʀᴇᴀꜱᴏɴ ʙᴏᴛʜ.


/settings - ᴛᴏ ᴄʜᴀɴɢᴇ ᴏʀ ᴇᴅɪᴛ ʙᴀꜱɪᴄ ꜱᴇᴛᴛɪɴɢꜱ ᴏꜰ ᴀꜰᴋ ʙᴏᴛ.
"""

def settings_markup(status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text="ᴄʟᴇᴀɴ ᴍᴏᴅᴇ", callback_data="cleanmode_answer"),
            InlineKeyboardButton(
                text="ᴇɴᴀʙʟᴇᴅ" if status == True else "❌ Disabled",
                callback_data="CLEANMODE",
            ),
        ],
        [
            InlineKeyboardButton(text="ᴄʟᴏꜱᴇ", callback_data="close"),
        ],
    ]
    return buttons
