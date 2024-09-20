import aiohttp
from data.config import ADMINS
from loader import bot
import requests
import instaloader

def download_instagram(url):
    try:
        L = instaloader.Instaloader()

        post_id = url.split('/')[-2]
        post = instaloader.Post.from_shortcode(L.context, post_id)

        if not post.video_url:
            return "No video links found."

        return post.video_url

    except Exception as e:
        print(f"Error retrieving video info: {e}")
        return str(e)  # Return the error message as a string
