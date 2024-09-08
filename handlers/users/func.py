import aiohttp
async def download_instagram(url):
    urls = "https://social-media-video-downloader.p.rapidapi.com/smvd/get/instagram"

    querystring = {"url": url}

    headers = {
        "x-rapidapi-key": "54e518fa11msha164dc2cecb21c8p18d479jsn65ee0a8c6b70",
        "x-rapidapi-host": "social-media-video-downloader.p.rapidapi.com"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=querystring) as response:
            if response.status == 200:
                data = await response.json()
                links = data.get('links', [])
                print(links)
                if links:
                    video_link = links[-1].get('link')
                    return video_link
                else:
                    return "No video links found."
            else:
                return f"Error: {response.status}"

