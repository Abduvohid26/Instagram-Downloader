import asyncio
from aiogram.filters import CommandStart
from loader import dp, bot, db
from aiogram import types, F, html
from filters.instagram_check_url import CheckInstaLink
from .func import download_instagram
from keyboards.inline.buttons import button, friend_connect
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
async def test(message: types.Message):
    link = message.text
    video_url, caption = download_instagram(link=link)
    try:
        if video_url:
            data = await bot.send_message(chat_id=message.from_user.id, text='Yuklanmoqda...')
            for i in range(1, 11):
                percent = i * 10
                white = '⬛️'
                black = '⬜️'
                await data.edit_text(text=f'{i * black}{white * (10 - i)}\n'
                                          f'{percent}% yuklandi')
                await asyncio.sleep(0.5)
            await data.delete()

            await message.answer_video(video=video_url, caption=f'{link}\n\n'
                                                                f'📥 {html.link(value="Instagram downloader", link="https://t.me/instgram_downloader_bot")}',
                                       reply_markup=friend_connect())
            msg = await message.answer('Tayyor')
            await asyncio.sleep(1)
            await msg.delete()
        else:
            await message.answer(text='Nimadur xato ketti')
    except Exception as e:
        print(e)

@dp.message(F.text)
async def test1(message: types.Message):
    await message.answer('Iltimos instgram link yuboring')

@dp.message(F.photo)
async def test1(message: types.Message):
    await message.answer('Iltimos instgram link yuboring')


@dp.message(F.video)
async def test1(message: types.Message):
    await message.answer('Iltimos instgram link yuboring')


