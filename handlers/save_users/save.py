import time
import csv
import os
from loader import bot, db
from aiogram import types
from data.config import ADMINS

async def save_users():
    data = db.select_all_users()
    custom_file_name = f'users_{int(time.time())}.csv'
    with open(custom_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'fullname', 'telegram_id', 'language'])
        for user in data:
            writer.writerow([user[0], user[1], user[2], user[3]])
    f = types.input_file.FSInputFile(path=custom_file_name, filename='Abduvohid.csv')
    for i in ADMINS:
        await bot.send_document(document=f, chat_id=i)
    try:
        if os.path.isfile(custom_file_name):
            os.remove(custom_file_name)
    except Exception as e:
        print(e)
        pass
    for i in ADMINS:
        await bot.send_message(chat_id=i, text='Userlar saqlandi')
