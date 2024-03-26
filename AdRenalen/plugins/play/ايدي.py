import pyrogram
from pyrogram import Client, filters

@app.on_message(filters.command('id'))
def ids(client: Client, message: Message):
    elketib = message.reply_to_message
    if elketib:
        message.reply_text(
            f"Name: {message.from_user.mention()}\nid: {massage.from_user.id}\nUserName: @{massage.from_user.username}"
        )
    else:
        message.reply(
            f"Name: {message.from_user.mention()}\nYour id: {message.from_user.id}"
        )
