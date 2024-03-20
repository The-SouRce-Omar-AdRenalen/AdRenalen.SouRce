from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AdRenalen import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/WA_ADRENALEN": 
        return
    try:
        try:
            await bot.get_chat_member("WA_ADRENALEN", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/WA_ADRENALEN".isalpha():
                link = "https://t.me/WA_ADRENALEN"
            else:
                chat_info = await bot.get_chat("WA_ADRENALEN")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"مرحبا عزيزي ↫ {msg.from_user.mention} \nعليك الاشتراك في قناة السورس اولا 💘 ⋅",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("• ⌯ 𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"JOIN ChaT @WA_ADRENALEN !")
      
