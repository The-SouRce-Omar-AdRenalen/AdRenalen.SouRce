import asyncio
import random
from AdRenalen import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


Omar = ["صلي علي النبي وتبسم", "بتكلمني انا", "معرفش🤔", "اللي ضاع من عمرو سنين نيهه😹", "انت متعرفنيش بجد اخص علي الصحب؟!"]

@app.on_message(filters.text & ~filters.edited & filters.regex(r"(^|.|$)"))
async def Omarmusic(client, message):
    if "مين" in message.text:
        response = random.choice(Omar)
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس", url="https://t.me/Omar_5")]])
        await message.reply(response, reply_markup=keyboard)

print("OKAY Omar MUSIC CODE WORKING NOW⚡")

