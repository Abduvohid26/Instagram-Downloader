import time
import csv
import os
from loader import bot, dp, db
from aiogram import types
from data.config import ADMINS


async def save_users():
    data = db.select_all_users()
    custom_file_name = f'main.csv'
    with open(custom_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'fullname', 'telegram_id', 'language'])
        for user in data:
            writer.writerow([user[0], user[1], user[2], user[3]])
    f = types.input_file.FSInputFile(path=custom_file_name, filename='Abduvohid.csv')
    for i in ADMINS:
        await bot.send_document(document=f, chat_id=i)
    for i in ADMINS:
        await bot.send_message(chat_id=i, text='Userlar saqlandi')


async def read_user_write_to_database():
    custom_file_name = 'main.csv'
    if os.path.isfile(custom_file_name):
        with open(custom_file_name, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if db.select_user(id=row['id']):
                    pass
                else:
                    id = row['id']
                    fullname = row['fullname']
                    telegram_id = row['telegram_id']
                    language = row['language']
                    db.add_user(id=id, fullname=fullname, telegram_id=telegram_id, language=language)

        for i in ADMINS:
            await bot.send_message(text='Bot qayta ishga tushdi va malumotlar tiklandi', chat_id=i)

        try:
            if os.path.isfile(custom_file_name):
                os.remove(custom_file_name)
        except Exception as e:
            print(e)
            pass
    else:
        pass
