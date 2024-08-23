import requests


def download_instagram(link):
		url = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/get-info-rapidapi"
		querystring = {"url": link}
		headers = {
			"x-rapidapi-key": "54e518fa11msha164dc2cecb21c8p18d479jsn65ee0a8c6b70",
			"x-rapidapi-host": "instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com"
		}
		response = requests.get(url, headers=headers, params=querystring)
		if response.status_code == 200:
			data = response.json()
			download_url = data.get('download_url', None)
			caption = data.get('caption', '')
			if download_url:
				return download_url, caption
		return None, None

