from aiogram.utils.keyboard import InlineKeyboardBuilder


def button():
    btn = InlineKeyboardBuilder()
    btn.button(text='♻️ Dostlarga ulashish', switch_inline_query='Instagram Downloader')
    btn.adjust(1)
    return btn.as_markup()


def friend_connect():
    btn = InlineKeyboardBuilder()
    btn.button(text='♻️ Dostlarga ulashish', switch_inline_query='Instagram Downloader')
    btn.adjust(1)
    return btn.as_markup()




def bot_button():
    btn = InlineKeyboardBuilder()
    btn.button(text="📥 Instagram downloader", url="https://t.me/instgram_downloader_bot")
    return btn.as_markup()