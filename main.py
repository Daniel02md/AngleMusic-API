from YoutubeAPI.youtube import YoutubeMusic
from Authentication.auth import Auth
from flask import Flask, request, Response, render_template
from flask_cors import cross_origin
from Extractor.extractor import Extractor
from functools import wraps
import asyncio



def asyncFunc(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        return asyncio.run(func(*args, **kwargs))
    return wrapped

app = Flask(__name__, template_folder='./', )



@app.route('/search', methods=["GET"])
@cross_origin()
@asyncFunc
async def search() -> Response:
    query = request.args.get('q')
    maxResults = request.args.get('maxResults', default=12)
    creds = Auth().loginYoutube()
    yt = YoutubeMusic(
        creds=creds
        )
    response = yt.search(
        q = query,
        maxResults = int(maxResults)
    )
    
    return Response(response=response, mimetype='application/json', content_type='application/json')


@app.route('/directLink', methods=["GET"])
@cross_origin()
@asyncFunc
async def directLink():
    link = request.args.get('url')
    directLink = Extractor.getDirectURL(link)
    return Response(response=directLink, mimetype='application/json')

app.run()