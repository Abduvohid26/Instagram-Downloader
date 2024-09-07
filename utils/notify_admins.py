from loader import bot
from data.config import ADMINS
from handlers.save_users.save import save_users, read_user_write_to_database
async def start():
    await read_user_write_to_database()
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