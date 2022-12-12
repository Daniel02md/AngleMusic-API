from json import dumps
from youtube_dl.YoutubeDL import YoutubeDL
import youtube_dl.utils
import requests

class Extractor:
    def __init__(self) -> None:
        pass

    @staticmethod
    def getDirectURL(uriVideo) -> dict:
        payloads = {
            'q': uriVideo,
            'vt' :'mp3'
        }   
        s = requests.Session()
        res = s.post('https://snapinsta.io/api/ajaxSearch', data=payloads).json()
        url = 'https://he61.aadika.xyz/download'+"/"+\
                res['vid']+"/"+\
                res['links']['mp3']['3']['f']+"/"+\
                res['links']['mp3']['3']['k']+"/"+\
                res['timeExpires']+"/"+\
                res['token']+"/1?f=SnapInsta.io"

        return dumps({"url": url})