#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅
import asyncio
from asyncio import gather
import os
import time
import requests
from pyrogram import enums
from pyrogram import types
import aiohttp
from pyrogram.types import CallbackQuery
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AdRenalen import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AdRenalen import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait


##############################################################
##############################################################
@app.on_message(filters.command(["سورس","السورس,","مصنع","صانع","مطور,","مطور السورس","المطور"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://d.top4top.io/m_30038easz0.mp4",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n\n- 𝐓𝐇𝐄 𝐁𝐄𝐒𝐓 𝐁𝐎𝐓 𝐎𝐍 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐒𝐔𝐏𝐄𝐑 𝐅𝐀𝐒𝐓 𝐀𝐍𝐃 𝐇𝐈𝐆𝐇 𝐀𝐂𝐂𝐔𝐑𝐀𝐂𝐘 ❤️🌿 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ 𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄.𝐎𝐌𝐀𝐑 › ", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ›", url=f"https://t.me/WA_AdRenalen"), 
                    InlineKeyboardButton(
                        "‹ 𝐒𝐔𝐏𝐏𝐔𝐑𝐓 ›", url=f"https://t.me/BAR_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["حمو المرازي","حمو"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/71e9ee5da45196ec2a5b0.jpg",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n- حمو المرازي الـ شء 💘😂 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AdRenalen"),
                ],[
                    InlineKeyboardButton(
                        "⌯ حمو الـ مرازي 💘 ⋅ ⌯", url=f"https://t.me/H4_il"), 
                    InlineKeyboardButton(
                        "⌯ ع ــمر ادرينالين 💘 ⋅ ⌯", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["سحس","حسين"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f6f7e37a411a115641e56.jpg",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n- حسين الـ شء 💘😂 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AdRenalen"),
                ],[
                    InlineKeyboardButton(
                        "⌯ حسين الحوب 💘 ⋅ ⌯", url=f"https://t.me/Hh_Uu_SS_Ee_Ii_Nn"), 
                    InlineKeyboardButton(
                        "⌯ ع ــمر ادرينالين 💘 ⋅ ⌯", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["صولو","سولو"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo( 
      photo=f"https://telegra.ph/file/81471e464fd78152dbdec.jpg",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n- سولو الـ شء 💘😂 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AdRenalen"),
                ],[
                    InlineKeyboardButton(
                        "⌯ سولو الـ تونز 💘 ⋅ ⌯", url=f"https://t.me/HA_RY2"), 
                    InlineKeyboardButton(
                        "⌯ ع ــمر ادرينالين 💘 ⋅ ⌯", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["فرعون","حرب"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo( 
      photo=f"https://telegra.ph/file/1d76ff4496515c122c251.jpg",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n- فرعون الـ شء 💘😂 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AdRenalen"),
                ],[
                    InlineKeyboardButton(
                        "⌯ فـرعون الـ تونز 💘 ⋅ ⌯", url=f"https://t.me/DEV_FAR3ON"), 
                    InlineKeyboardButton(
                        "⌯ ع ــمر ادرينالين 💘 ⋅ ⌯", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )
     


    
@app.on_message(filters.command(["عمر فيرس","فيرس"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo( 
      photo=f"https://telegra.ph/file/783c1ff05a1480c023f9e.jpg",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n- فيرس الـ شء 💘😂 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AdRenalen"),
                ],[
                    InlineKeyboardButton(
                        "⌯ فيرس الـ تونز 💘 ⋅ ⌯", url=f"https://t.me/Xx_VAiRS_xX"), 
                    InlineKeyboardButton(
                        "⌯ ع ــمر ادرينالين 💘 ⋅ ⌯", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )





iddof = []
id = {}

@app.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "") & filters.group)
async def iddlock(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in iddof:
            return await message.reply_text("♪ الامر معطل من قبل 💎 .")
        iddof.append(message.chat.id)
        return await message.reply_text("♪ تم تعطيل الايدي بنجاح 💎 .")
    else:
        return await message.reply_text("♪ عذرا عزيزي هذا الامر للادمن الجروب فقط 💎 .")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "") & filters.group)
async def iddopen(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in iddof:
            return await message.reply_text("♪ الايدي مفعل من قبل 💎 .")
        iddof.remove(message.chat.id)
        return await message.reply_text("♪ تم تفعيل الايدي بنجاح 💎 .")
    else:
        return await message.reply_text("♪ عذرا عزيزي هذا الامر للادمن الجروب فقط 💎 .")

@app.on_message(filters.command(["ايدي"], ""))
async def muid(client: Client, message):
    if message.chat.id in iddof:
        return await message.reply_text("♪ تم تعطيل امر الايدي من قبل المشرفين 💎 .")
    
    user = await client.get_chat(message.from_user.id)
    user_id = user.id
    username = user.username
    first_name = user.first_name
    bioo = user.bio
    
    photo = user.photo.big_file_id
    if photo:
        photo = await client.download_media(photo)
    else:
        photo = None
    
    if user.id not in id:
        id[user.id] = []
    
    idd = len(id[user.id])
    
    caption = f"name : {first_name}\nid : {user_id}\nuser : [@{username}]\nbio : {bioo}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{user_id}")]])
    
    await message.reply_photo(photo=photo, caption=caption, reply_markup=reply_markup)

@app.on_callback_query(filters.regex("heart"))
async def heart(client, query: CallbackQuery):
    callback_data = query.data.strip()
    callback_request = callback_data.replace("heart", "")
    username = int(callback_request)
    usr = await client.get_chat(username)
    
    if usr.id not in id:
        id[usr.id] = []
    
    if query.from_user.mention not in id[usr.id]:
        id[usr.id].append(query.from_user.mention)
    else:
        id[usr.id].remove(query.from_user.mention)
    
    idd = len(id[usr.id])
    
    caption = f"name : {usr.first_name}\nid : {usr.id}\nuser : [@{usr.username}]\nbio : {usr.bio}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{usr.id}")]])
    
    await query.edit_message_text(caption, reply_markup=reply_markup)

@app.on_message(filters.command(["اسمي","اسمي اي","قول اسمي"], ""), group=123222)
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""- اسمك » ⦗ {message.from_user.mention} ⦘ 💘 ⋅""") 

##############################################################
##############################################################
##############################################################
  


#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅    
