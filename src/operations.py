# here we instatiate the calls for both chatgpt and AWS

from langchain import OpenAI
from src.utils.common import read_yaml

from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.agents import Tool
from src.custom_toolkit import WeatherTool, awsEC2Tool, DummyTool

config = read_yaml("config.yaml")

MODEL_NAME = config['chatbot'][os.environ['MODEL_NAME']]
TEMPERATURE = config['chatbot'][os.environ['TEMPERATURE']]

# here we instantiate the OpenAI object 
LLM_Object = OpenAI(
    model_name = os.environ['MODEL_NAME'],
    temperature = os.environ['TEMPERATURE']
)

search = SerpAPIWrapper()
LLM_math_chain = LLMMathChain(LLM_Object=LLM_Object, verbose=True)

def get_conv_agent():
    tools = [awsEC2Tool(), WeatherTool()]
    tools.append(
        Tool.from_function(
            func = search.run,
            name = "Search",
            description = "experimental chatgpt running with python and twinkle, useful to ask about the news or weather"
        )
    )

    tools.append(
        Tool.from_function(
            func = search.run,
            name = "Calculator",
            description = "experimental chatgpt running with python and twinkle, useful to ask about math"
        )
    )

    tools.append(DummyTool())

    conv_agent = initialize_agent(
        agent = AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        tools = tools,
        LLM_Object = LLM_Object,
        verbose = True,
        max_iterations = 3,
        early_stopping_method = 'generate',
        handle_parsing_errors = "The chain should end with the reply from chatgpt"
    )

    conv_agent.agent.llm_chain.prompt.messages[0].prompt.template = f"""
        AI chatbot developed by Jose Miguel Vazquez Mendez.
        "System:"\n
        {str(conv_agent.agent.llm_chain.prompt.messages[0].prompt.template)}\n
        The final answer should be sent as a string.
    """
    return conv_agent