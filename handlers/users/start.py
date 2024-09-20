import asyncio
from aiogram.filters import CommandStart
from loader import dp, bot, db
from aiogram import F, html, suppress
from filters.instagram_check_url import CheckInstaLink
from keyboards.inline.buttons import button, friend_connect
from middlewares.my_middleware import CheckSubCallback
from utils.misc.subscription import checksubscription
from data.config import CHANNELS
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
import asyncio
from aiogram import types
from .func import download_instagram
from aiogram.enums.chat_action import ChatAction

@dp.message(CommandStart())
async def start_bot(message: types.Message):
    current_user = message.from_user.id
    try:
        if db.select_user(id=current_user):

            await message.answer(
                f"Assalomu alaykum {message.from_user.full_name}!\n\n"
                f"Ushbu bot yordamida Instagramdan video yuklab olishingiz mumkin.",
                reply_markup=button()
            )
        else:
            db.add_user(id=current_user, fullname=message.from_user.full_name, telegram_id=current_user, language=message.from_user.language_code)
    except Exception as e:
        print(e)


@dp.message(F.text, CheckInstaLink())
async def handle_instagram_video(message: types.Message):
    link = message.text
    user_id = message.from_user.id

    loading_message = await bot.send_message(
        chat_id=user_id,
        text='📹 Video serverdan yuklanmoqda\nIltimos biroz kuting !'
    )

    try:
        video_link = download_instagram(link)

        if not video_link or "Error" in video_link:
            await bot.send_message(chat_id=user_id, text="Video topilmadi yoki yuklashda xato yuz berdi.")
            return

        progress_message = await bot.send_message(chat_id=user_id, text='Yuklanmoqda...')
        await loading_message.delete()

        for i in range(1, 11):
            percent = i * 10
            progress_bar = '⬛️' * i + '⬜️' * (10 - i)
            await progress_message.edit_text(text=f'{progress_bar}\n{percent}% yuklandi')
            await asyncio.sleep(0.1)

        await progress_message.delete()
        await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.UPLOAD_VIDEO)
        await bot.send_video(
            chat_id=user_id,
            video=video_link,
            caption=f'{link}\n\n📥 {html.link(value="Instagram downloader", link="https://t.me/instgram_downloader_bot")}',
            reply_markup=friend_connect()
        )

        final_message = await message.answer('Tayyor')
        await message.delete()
        await asyncio.sleep(0.5)
        await final_message.delete()

    except Exception as e:
        await bot.send_message(chat_id=user_id, text=f"Xatolik yuz berdi: {str(e)}")
        print(e)
    finally:
        # Ensure loading message is deleted in case of errors
        await loading_message.delete()
        
@dp.message(F.text)
async def test1(message: types.Message):
    await message.answer('Iltimos instgram link yuboring')

@dp.message(F.photo)
async def test1(message: types.Message):
    await message.answer('Iltimos instgram link yuboring')


@dp.message(F.video)
async def test1(message: types.Message):
    await message.answer('Iltimos instgram link yuboring')



@dp.callback_query(CheckSubCallback.filter())
async def check_query(call: types.CallbackQuery):
    await call.answer(cache_time=0)  # Har safar callback query ga javob
    user = call.from_user
    final_status = True
    btn = InlineKeyboardBuilder()

    if CHANNELS:
        for channel in CHANNELS:
            try:
                status = await checksubscription(user_id=user.id, channel=channel)
                final_status = final_status and status
                chat = await bot.get_chat(chat_id=channel)
                invite_link = await chat.export_invite_link()
                btn.button(
                    text=f"{'✅' if status else '❌'} {chat.title}",
                    url=invite_link
                )
            except Exception as e:
                print(f"Kanalga kirish yoki linkni olishda xato: {e}")

        if final_status:
            await call.message.answer(
                f"Assalomu alaykum {call.from_user.full_name}!\n\n"
                f"Marhamat, botdan foydalanishingiz mumkin.",
                reply_markup=button()
            )
        else:
            btn.button(
                text="🔄 Tekshirish",
                callback_data=CheckSubCallback(check=False)
            )
            btn.adjust(1)
            data = await call.message.answer(
                text="Iltimos avval barcha kanallarga azo boling !"
            )
            await asyncio.sleep(5)
            await data.delete()
    else:
        await call.message.answer(
            f"Assalomu alaykum {call.from_user.full_name}!\n\n"
            f"Marhamat, botdan foydalanishingiz mumkin.",
            reply_markup=button()
        )