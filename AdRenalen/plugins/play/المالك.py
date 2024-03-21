import asyncio
import os
from pyrogram import filters
from pyrogram import Client
from AdRenalen import app


@app.on_message(filters.command(["اسمي","اسمي اي"], ""), group=123222)
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""- اسمك » ⦗ {message.from_user.mention} ⦘ 💘 ⋅""") 
