from pyrogram import Client, idle
#'‹ ٰ💸 ⇣ سورس الفراعنة ⇣ 💸 › .'#
from pyromod import listen



bot = Client(
    "mo",
    api_id=26566005,
    api_hash="690c0394fc7bf850afd91ab0f66160b2",
    bot_token="6992462567:AAErJZyTSWLQ-of-L80suo5nU0FjmIMJf20",#توكن المصنع
    plugins=dict(root="MHelal")
    )

async def start_helalbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    hh = "DEV_AdRenalen"#يوزر المطور المصنع
    try:
        await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
    except:
        pass
    await idle()
