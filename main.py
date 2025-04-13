import logging
from utils import agentUtils, myLogger, spotifyUtils
from api import spotifyAPI

def runSpotifyAPI():
    myLogger.debug('runSpotifyAPI - getting token')
    t = spotifyUtils.getToken()
    myLogger.debug('runSpotifyAPI - getting user profile for user: {}'.format(spotifyAPI.SPOTIFY_USER))
    u = spotifyAPI.getUserProfile(t, spotifyAPI.SPOTIFY_USER)
    userString = 'Here is more information about {}:\n\tName: {}\n\tFollower Count: {}'.format(
            spotifyAPI.SPOTIFY_USER, 
            u['display_name'], 
            u['followers']['total']
        )
    output = '\n------------------------\nAPI OUTPUT:\n{}\n------------------------'.format(userString)
    print(output)
    myLogger.debug(output)

def runSpotifyAgent():
    myLogger.debug('runSpotifyAgent - get agent')
    agent = agentUtils.getAgent()

    input_text='tell me about user {}'.format(spotifyAPI.SPOTIFY_USER)
    
    myLogger.debug('runSpotifyAgent - run agent with input: {}'.format(input_text))
    result = agent(input_text)
    serialized_agent_response = agentUtils.serializeAgentResponse(result)
    myLogger.debug('runSpotifyAgent - serialized response : \n{}'.format(serialized_agent_response))
    userString = serialized_agent_response['output']
    output = '\n------------------------\nAGENT OUTPUT:\n{}\n------------------------'.format(userString)
    print(output)
    myLogger.debug(output)

def main():
    try:
        myLogger.LogLevel.initLogger(logging.DEBUG)
        myLogger.info('MAIN - start')
        myLogger.debug('MAIN - get output via API')
        runSpotifyAPI()
        myLogger.debug('MAIN - get output via agent')
        runSpotifyAgent()
    except Exception as e:
        myLogger.error('MAIN - error. \n{}'.format(e))
        print(e)
        raise e
    myLogger.info('MAIN - done')
    return 0

if __name__ == '__main__':
    myLogger.debug(main())

    