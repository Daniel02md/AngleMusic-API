from json import dumps
from isodate import parse_duration
from datetime import timedelta
class YoutubeMusic:
    __MUSIC_CATEGORY_ID = 10
    
    def __init__(self, creds) -> None:
        self.creds = creds
        

    def search(self, q, maxResults=10):
        self.service = self.creds
        request = self.service.search().list(
                part = 'snippet',
                order = 'viewCount',
                q = q,
                type = 'video',
                maxResults = maxResults,
                videoCategoryId = self.__MUSIC_CATEGORY_ID
        )
        
        response = request.execute()
        
        return self.__modelDataSearch(response)



    def __modelDataSearch(self, searchResult):
        
        newSearchResultList = list()
        YT_BASE_URL = 'https://youtube.com/watch?v='
        for result in searchResult['items']:
            duration = self.service.videos().list(
                    part = 'contentDetails',
                    id = result['id']['videoId']
            )

            
            duration = duration.execute()
            
            duration = duration['items'][0]['contentDetails']['duration']
            duration = int(parse_duration(duration).total_seconds())
            duration = str(timedelta(seconds=duration))
            newResult = {} 
            newResult = result['snippet']
            newResult['videoUrl'] = f"{YT_BASE_URL}{result['id']['videoId']}"
            newResult['videoId'] = result['id']['videoId']
            newResult['duration'] = duration

            newSearchResultList.append(newResult)
        return dumps(newSearchResultList)
