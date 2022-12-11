from json import dumps
from youtube_dl.YoutubeDL import YoutubeDL
import youtube_dl.utils

class Extractor:
    def __init__(self) -> None:
        pass

    @staticmethod
    def getDirectURL(uriVideo) -> str:
        directLink = {}
        yt_opts = {
            'format': '140/bestaudio',
            'quiet': True
        }   
        youtube_dl.utils.std_headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

        yt_dl = YoutubeDL(yt_opts)
        arrayformats = yt_dl.extract_info(uriVideo.replace('"', ''), download=False)['formats']
        for item in arrayformats:
            if item['format_id'] == '140':
                directLink['url'] = item['url']
                break

        return dumps(directLink)