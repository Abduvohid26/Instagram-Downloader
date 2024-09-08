import aiohttp
from data.config import ADMINS
from loader import bot
async def download_instagram(url):
    api_url = "https://social-media-video-downloader.p.rapidapi.com/smvd/get/instagram"
    querystring = {"url": url}
    headers = {
        "x-rapidapi-key": "54e518fa11msha164dc2cecb21c8p18d479jsn65ee0a8c6b70",
        "x-rapidapi-host": "social-media-video-downloader.p.rapidapi.com"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url, headers=headers, params=querystring) as response:
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                data = await response.json()
                links = data.get('links', [])
                if links:
                    video_link = links[1].get('link')
                    return video_link
                else:
                    return "No video links found."
            else:
                return f"Unexpected content type: {content_type}"
