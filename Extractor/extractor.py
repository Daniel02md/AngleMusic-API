from json import dumps
from youtube_dl.YoutubeDL import YoutubeDL


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
        yt_dl = YoutubeDL(yt_opts)
        arrayformats = yt_dl.extract_info(uriVideo.replace('"', ''), download=False)['formats']
        for item in arrayformats:
            if item['format_id'] == '140':
                directLink['url'] = item['url']
                break

        return dumps(directLink)