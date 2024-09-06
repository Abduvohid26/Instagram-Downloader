import aiohttp
async def download_instagram(link):
	url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
	querystring = {"url": link}
	headers = {
	 			"x-rapidapi-key": "54e518fa11msha164dc2cecb21c8p18d479jsn65ee0a8c6b70",
	 			"x-rapidapi-host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
	 		}

	async with aiohttp.ClientSession() as session:
		async with session.get(url, headers=headers, params=querystring) as response:
			if response.status == 200:
				data = await response.json()
				# Extracting the video URL and caption
				download_url = data.get('media', None)  # Fetches the media URL
				caption = data.get('title', '')  # Fetches the caption/title
				if download_url:
					return download_url, caption
	return None, None