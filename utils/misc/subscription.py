from loader import bot
from aiogram import types
from typing import Union
async def checksubscription(user_id,channel:Union[int,str]) -> bool:
    member = await bot.get_chat_member(chat_id=channel,user_id=user_id)
    status = member.status
    if status=='creator' or status=='administrator' or status=='member':
        return True
    else:
        return False

