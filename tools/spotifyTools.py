from langchain.tools import BaseTool
from api import spotifyAPI
from utils import myLogger

class spotifyUser(BaseTool):
    name = "User"
    description = "useful for when you need to get information about a user on spotify."

    def _run(self,username):
        """Use the tool."""
        response = spotifyAPI.getUserProfile(spotifyAPI.getToken(), username)

        return 'Here is more information about {}:\n\tName: {}\n\tFollower Count: {}'.format(
            username, 
            response['display_name'], 
            response['followers']['total']
        ) 

    def _arun(self, username):
        raise NotImplementedError("This tool does not support async")
    
def createTools():
    tools = [spotifyUser()]
    myLogger.info('creating {} Spotify Tools: [{}]'.format(len(tools), ','.join([t.name for t in tools])))
    return tools