from pyrogram import Client, filters, idle
from pyrogram.enums import ChatMemberStatus
from config *

mutes = []
@app.on_message(filters.command("dmute") & filters.group)
async def mute(app,message):
   member = await message.chat.get_member(message.from_user.id)
   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await message.reply("**Only chat admins can use this command**")
   else:
     if not message.reply_to_message:
       return await message.reply("**• You must reply to an user first**")
     member = await message.chat.get_member(message.reply_to_message.from_user.id)
     if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       return await message.reply("**You can't mute chat admin**")
     chat_id = str(message.chat.id)
     user_id = str(message.reply_to_message.from_user.id)
     x = "{}@{}".format(chat_id,user_id)
     if x in mutes:
       return await message.reply("**This user already muted in this chat**")
     else:
       mutes.append(x)
       return await message.reply("**{} has muted successfully by {} .**".format(message.reply_to_message.from_user.mention,message.from_user.mention))
       
@app.on_message(filters.command("undmute") & filters.group)
async def unmute(app,message):
   member = await message.chat.get_member(message.from_user.id)
   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await message.reply("**Only chat admins can use this command**")
   else:
     if not message.reply_to_message:
       return await message.reply("**• You must reply to an user first**")
     member = await message.chat.get_member(message.reply_to_message.from_user.id)
     if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       return await message.reply("**You can't unmute chat admin**")
     chat_id = str(message.chat.id)
     user_id = str(message.reply_to_message.from_user.id)
     x = "{}@{}".format(chat_id,user_id)
     if not x in mutes:
       return await message.reply("**This user already unmuted in this chat**")
     else:
       mutes.remove(x)
       return await message.reply("**{} has unmuted successfully by {} .**".format(message.reply_to_message.from_user.mention,message.from_user.mention))

@app.on_message(filters.command("dmutes") & filters.group)
def get_dmute(app, message):
   if len(mutes) == 0: return
   member = message.chat.get_member(message.from_user.id)
   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return message.reply("**Only chat admins can use this command**")
   ch = message.chat.id
   c = 0
   text = "• Mutes list in this chat :\n\n"
   for a in mutes:
     chat_id = int(a.split("@")[0])
     user_id = int(a.split("@")[1])
     if chat_id == ch:
        user = app.get_users(user_id)
        text += f"- {user.mention}\n"
        c += 1
   if c == 0: return message.reply("**No one muted in this chat**")
   message.reply(f"**{text}**")

@app.on_message(filters.group)
def del_msg(_,m):
   if m.from_user:
     chat_id = str(m.chat.id)
     user_id = str(m.from_user.id)
     x = "{}@{}".format(chat_id,user_id)
   for a in mutes:
     if a == x: 
       m.delete()
       break


app.start()
print("✓✓✓")
idle()
