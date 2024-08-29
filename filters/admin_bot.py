from aiogram.filters import BaseFilter
from aiogram import types
from data.config import ADMINS
class IsBotAdmin(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return str(message.from_user.id) in ADMINS