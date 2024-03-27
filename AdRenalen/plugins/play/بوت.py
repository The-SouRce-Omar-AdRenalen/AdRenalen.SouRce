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

name = "ادرينالين"

@app.on_message(filters.regex("تعيين اسم البوت")& filters.private & SUDOERS, group=7113)
async def set_bot_name(client, message):
    global name
    ask = await app.ask(message.chat.id, "ارسل الاسم الجديد", timeout=300)
    name = ask.text
    await message.reply_text("تم تعيين الاسم بنجاح")

caesar_responses = [
    "اسمي {name} يصحبي 💘 ⋅",
    "يسطا قولتلك اسمي {name } ☺️",
    "اي يزميلي 😂♥️ ،",
    "قلب البوت 🥹💘 ⋅",
    "ثانية بشقط التنية 😂💘 ،",
    "يعم والله بحبك بس ناديلي ب {name} 🙂",
    "اي ي معلم مين مزعلك",
    "ايوا جاااي 😂♥️ ،",
    "تبا لك ماذا تريد من امي 🙂",
]

@app.on_message(filters.command(["بوت", "البوت"], ""), group=71135)
async def caesar_bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(caesar_responses).format(name=name)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])
    
    await message.reply_text(
        text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**",
        disable_web_page_preview=True,
        reply_markup=keyboard,
    parse_mode=enums.ParseMode.MARKDOWN)




Sla_nem = {}

elecm = "يصحبي"

@app.on_message(filters.regex("تعين الصلاة علي النبي")& filters.private & SUDOERS, group=7113)
async def set_Sla_nem(client, message):
    global elecm
    ask = await app.ask(message.chat.id, "ارسل الاسم الجديد", timeout=300)
    elecm = ask.text
    await message.reply_text("تم تعيين الاسم بنجاح")

caesar_responses = [
    "صلي علي النبي وتبسم ♥️♥️♥️♥️!",
    "صلي علي النبي وتبسم {elecm} ♥️♥️♥️♥️!",
]

@app.on_message(filters.command(["⋅","ـ",".","..","..."], ""), group=71135)
async def caesar_bot(client, message):
    global elecm
    bot_username = (await app.get_me()).username
    bar = random.choice(caesar_responses).format(elecm=elecm)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("صلي علي النبي وتبسم ♥️♥️!", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])
    
    await message.reply_text(
        text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**",
        disable_web_page_preview=True,
        reply_markup=keyboard,
    parse_mode=enums.ParseMode.MARKDOWN)
