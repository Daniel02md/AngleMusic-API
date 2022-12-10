from pytube import YouTube
from pytube.exceptions import LiveStreamError
from json import dumps



class Extractor:
    def __init__(self) -> None:
        pass

    @staticmethod
    def getDirectURL(uriVideo) -> str:
        directLink = {}
        try:
            url = YouTube(uriVideo).streams.get_audio_only().url
        except LiveStreamError:
            directLink['error'] = {'errorMessage': 'The selected music is a LiveStream.'}
        except Exception as e:
            directLink['error'] = {'errorMessage': f'{repr(e)}'}

        else:
            directLink['url'] = url
            
        finally: 
            return dumps(directLink)