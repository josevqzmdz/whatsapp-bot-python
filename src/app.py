# 'main' application

from typing import Union
from dotenv import load_dotenv
from flask import Flask, request
from wsgiref import simple_server
from flask_cors import CORS, cross_origin
import openai
import os

from twilio.twiml.messaging_response import MessagingResponse 
from src.operations import get_conv_agent
from src.utils.common import read_yaml
import os

# runs .NET framework
load_dotenv()

# runs the yaml wrapper in case this thing is run as a docker container

config = read_yaml('src/config.yaml')

APP_HOST = config['serving'][os.environ('APP_HOST')]
APP_PORT = config['serving'][os.environ('APP_PORT')]

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# starts Flask's micro API
app = Flask(__name__)
# makes this API CORS-friendly
CORS(app)

# makes a call to chatgpt and gets an answer whenever the user sends an input
def generate_answer(question: str):
    conv_agent = get_conv_agent()
    # LLM / chatgpt
    llm_response = conv_agent(question)

    if 'output' in llm_response:
        output = llm_response['output']
    elif 'action_input' in llm_response:
        output = llm_response['action_input']
    else:
        output = llm_response
    return output

# define a route to handle incoming requests
@app.route('/chatgpt_webhook', methods=['POST'])
@cross_origin()
def chatgpt():
    incoming_queue = request.values.get('Body', '')
    print("question: ", incoming_queue)
    print("BOT ANSWER: ", answer)
    bot_response = MessagingResponse()
    message = bot_response.message()
    message.body(answer)
    return str(bot_response)

# run the flask app
if __name__ == '__main__':
    httpd = simple_server.make_server(
        host=APP_HOST,
        port=APP_PORT,
        app=app
    )
    httpd.serve_forever()