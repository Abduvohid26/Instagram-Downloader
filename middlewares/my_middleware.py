from aiogram import BaseMiddleware
from aiogram.types import Message,Update
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import *
from loader import bot
from data.config import CHANNELS
from utils.misc.subscription import checksubscription
from aiogram.filters.callback_data import CallbackData
class CheckSubCallback(CallbackData,prefix='check'):
    check :bool
class UserCheckMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any]
    ) -> bool:
        btn = InlineKeyboardBuilder()
        user = event.from_user
        final_status = True
        print(CHANNELS)
        if CHANNELS:
            for channel in CHANNELS:
                status = True
                try:
                    status = await checksubscription(user_id=user.id, channel=channel)
                except Exception as e:
                    print(f"Subscription check error: {e}")

                final_status = final_status and status

                try:
                    chat = await bot.get_chat(chat_id=channel)
                    invite_link = await chat.export_invite_link()
                    button_text = f"✅ {chat.title}" if status else f"❌ {chat.title}"
                    btn.button(text=button_text, url=invite_link)
                except Exception as e:
                    print(f"Chat error: {e}")

            if final_status:
                await handler(event, data)
            else:
                btn.button(
                    text="🔄 Tekshirish",
                    callback_data=CheckSubCallback.new(check=False)  # To'g'ri formatda callback data yaratish
                )
                btn.adjust(1)
                await event.message.answer(
                    "Iltimos bot to'liq ishlashi uchun quyidagi kanal(lar)ga obuna bo'ling!",
                    reply_markup=btn.as_markup()
                )
        else:
            await handler(event, data)

