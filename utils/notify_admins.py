from loader import bot
from data.config import ADMINS
from handlers.save_users.save import save_users
async def start():
    for i in ADMINS:
        try:
            await bot.send_message(chat_id=i,text="Bot faollashdi!")
        except:
            pass
async def shutdown():
    await save_users()
    for i in ADMINS:
        try:
            await bot.send_message(chat_id=i,text="Bot to'xtadi!")
        except:
            pass