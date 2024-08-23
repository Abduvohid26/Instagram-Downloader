from aiogram.filters import BaseFilter
from aiogram import types

class CheckInstaLink(BaseFilter):
    async def __call__(self, message: types.Message):
        if message.text.startswith('https://instagram.com'):
            return True
        elif message.text.startswith('https://www.instagram.com'):
            return True

        elif message.text.startswith('http://instagram.com'):
            return True

        elif message.text.startswith('http://www.instagram.com'):
            return True
        else:
            return False
