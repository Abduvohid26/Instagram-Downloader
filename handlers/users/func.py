import instaloader
import os
from aiogram import types, html
from aiogram.types import InputFile

from loader import bot
loader = instaloader.Instaloader()
async def download_instagram(link, user_id):
    try:
        # Instagram post shortcode olish
        shortcode = link.split('/')[4]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        download_folder = f"{shortcode}"

        if post.is_video:
            # Faylni yuklash
            loader.download_post(post, target=download_folder)

            video_path = None
            for file in os.listdir(download_folder):
                if file.endswith(".mp4"):
                    video_path = os.path.join(download_folder, file)

            if video_path and os.path.exists(video_path):
                # Faylni to'g'ri ochish
                video = types.input_file.FSInputFile(video_path)

                # Fayllarni tozalash
                for file in os.listdir(download_folder):
                    os.remove(os.path.join(download_folder, file))
                os.rmdir(download_folder)

                return video, "Instagram video loaded successfully"

        else:
            await bot.send_message(text="Bu URL video emas, iltimos video URL kiriting.", chat_id=user_id)
            return None, None
    except Exception as e:
        await bot.send_message(text=f"Xatolik yuz berdi: {e}", chat_id=user_id)
        return None, None