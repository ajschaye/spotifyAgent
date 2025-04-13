from utils import myLogger
from tools import spotifyTools
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from requests.models import Response  

OPENAI_SECRET = '<ADD_SECRET>'

def getTools():
    myLogger.debug('getTools - create tools for agent')
    tools = []
    for t in spotifyTools.createTools():
        tools.append(t)
    return tools

def getAgent():
    myLogger.debug('getAgent - build agent')
    tools = getTools()
    print(tools)
    #import openai and set llm

    myLogger.debug('getAgent - initiate llm')
    llm = ChatOpenAI(openai_api_key=OPENAI_SECRET, temperature=0)
    myLogger.debug('getAgent - initiate agent')
    agent = initialize_agent(
        tools, 
        llm, 
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        max_iterations=6,
        handle_parsing_errors=True,
        verbose=True,
        max_execution_time=10,
        return_intermediate_steps=True
    )
    return agent

def serializeAgentResponse(agent_response):
    new_intermediate_steps = []

    for step in agent_response['intermediate_steps']:
        serialized_step = []

        for item in step:
            if isinstance(item, Response):
                serialized_item = {
                    'status_code': item.status_code,
                    'reason': item.reason,
                    'text': item.text  
                }
            else:
                serialized_item = item

            serialized_step.append(serialized_item)

        new_intermediate_steps.append(tuple(serialized_step))

    serialized_agent_response = agent_response.copy()
    serialized_agent_response['intermediate_steps'] = new_intermediate_steps

    return serialized_agent_response


#def getOpenAILLM():
#    return ChatOpenAI(openai_api_key=OPENAI_SECRET)
#llm = getOpenAILLM()
#text = "What would be a good company name for a company that makes colorful socks?"
#messages = [HumanMessage(content=text)]
#print(llm.invoke(text))
# >> Feetful of Fun
