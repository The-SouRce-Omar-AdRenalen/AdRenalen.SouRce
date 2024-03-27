import asyncio
import random
from pyrogram import enums
from pyrogram import types
from AdRenalen.misc import SUDOERS
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from AdRenalen import app
from config import *

bot_name = {}

name = "يصحبي"

@app.on_message(filters.regex("تعين الصلاة علي النبي")& filters.private & SUDOERS, group=7113)
async def set_bot_name(client, message):
    global name
    ask = await app.ask(message.chat.id, "ارسل الاسم الجديد", timeout=300)
    name = ask.text
    await message.reply_text("تم تعيين الاسم بنجاح")

caesar_responses = [
    "صلي علي النبي وتبسم ♥️♥️♥️♥️!",
    "صلي علي النبي وتبسم {name} ♥️♥️♥️♥️!",
    "صلي علي النبي وتبسم يرايق ♥️♥️!",
    "صلي علي قلبك يطيب ♥️♥️!",
    "صلي علي النبي وتبسم يزميلي ♥️♥️♥️♥️!",
    ]

@app.on_message(filters.command(["⋅","ـ",".","..","..."], ""), group=71135)
async def caesar_bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(caesar_responses).format(name=name)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("صلي علي النبي وتبسم ♥️♥️!", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])
    
    await message.reply_text(
        text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**",
        disable_web_page_preview=True,
        reply_markup=keyboard,
    parse_mode=enums.ParseMode.MARKDOWN)
