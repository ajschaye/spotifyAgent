import requests
from utils import myLogger

SPOTIFY_CLIENT_ID = '<ADD_CLIENT_ID>'
SPOTIFY_CLIENT_SECRET = '<ADD_CLIENT_SECRET>'
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_URL_BASE = 'https://api.spotify.com/v1'
SPOTIFY_USER = 'ajschaye'
SPOTIFY_SEARCH_CATS = ["album", "artist", "playlist", "track", "show", "episode", "audiobook"]

def getToken():
    myLogger.debug('api.spotifyAPI - getting token')
    auth_response = requests.post(
        SPOTIFY_AUTH_URL, 
        {
            'grant_type': 'client_credentials',
            'client_id': SPOTIFY_CLIENT_ID,
            'client_secret': SPOTIFY_CLIENT_SECRET,
        })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']
    myLogger.debug('api.spotifyAPI - token received')
    return access_token

def getHeader(access_token):
    return {
            'Authorization': 'Bearer {token}'.format(token=access_token)
        }

def callSpotifyGet(token, uri, params={}):
    header = getHeader(token)
    api_url = SPOTIFY_URL_BASE + uri
    myLogger.debug('api.spotifyAPI - calling api with \n\tURI: {}\n\tparams: {}'.format(api_url, params))
    rep = requests.get(api_url, headers=header, params=params).json()
    myLogger.debug('api.sportifyAPI - return from API: \n{}\n'.format(rep))
    return rep

#print(callSpotifyGet(getToken(), '/users/{}'.format(SPOTIFY_USER)))
