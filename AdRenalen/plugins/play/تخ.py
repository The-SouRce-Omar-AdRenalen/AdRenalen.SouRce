from strings.filters import command
from pyrogram import filters.group
import asyncio
from pyrogram import Client
from pyrogram import enums
from pyrogram import types
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AdRenalen import app


@app.on_message(command(["بيو بيو","بيو","تخ"],"") & filters.group)
async def huhh(client, message):
    to_id = int(Omar.split("to")[-1].split("in")[0])
    from_id = int(Omar.split("Omar")[-1].split("to")[0])
    in_id = int(caption.split("in")[-1])
    to_url = f"tg://openmessage?user_id={to_id}"
    from_url = f"tg://openmessage?user_id={from_id}"
    Omar = message.text
    await message.reply_video(
        video = "https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
        caption = "↯︙قتل ↫ ⦗ {app.get_chat(to_id).first_name}]({to_url}) ⦘\nالضحيه دا 😢 ↫ ⦗ {app.get_chat(from_id).first_name} ⦘\nانا لله وانـا اليـه راجعـون 😢😢",   
  reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton("‹ الـ قاتل  ›", url=f"{to_url}"), 
                ],[
                    InlineKeyboardButton("‹ الـ ضحية ›", url=f"{from_url}"),
                    InlineKeyboardButton(
                        "‹ 𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄 ›", url=f"http://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐂𝐇.𝐒𝐎𝐔𝐑𝐂𝐄 ›", url=f"http://t.me/WA_ADRENALEN"),
            ]
        ]                   

         ),parse_mode=enums.ParseMode.MARKDOWN)
