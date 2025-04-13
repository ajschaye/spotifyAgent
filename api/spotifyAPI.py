from utils.spotifyUtils import *

def getUserProfile(token, user):
    r = callSpotifyGet(token, '/users/{}'.format(user))
    return r

def getUserPlaylists(token, user):
    r = callSpotifyGet(token, '/users/{}/playlists'.format(user), {'limit' : 5})
    return r

def search(token, q, cat=SPOTIFY_SEARCH_CATS, params={}):
    uri = '/search?q={}&type={}'.format(q,','.join(cat))
    if len(params) > 0:
        uri = uri + '&' + '&'.join(['{}={}'.format(a,b) for a,b in params.items()])
    r = callSpotifyGet(token, uri)
    return r

#token = getToken()
#getUserProfile(token, SPOTIFY_USER)
#playlistJson = getUserPlaylists(token, SPOTIFY_USER)
#for p in playlistJson['items']:
#    print(p['name'])

#artistJson = search(token, 'U2', cat=['artist'], params={'limit':5})
#for a in artistJson['artists']['items']:
#    print(a['name'])
