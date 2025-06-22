import boto3
from dotenv import load_dotenv
from langchain.tools import BaseTool

load_dotenv()

ec2_client = boto3.client('ec2')

desc = """
    this tool exists solely to test if the app is running fine
    like a health check
    other than that is just a dummy request
"""

class DummyTool(BaseTool):
    name = "dummy tool"
    description = desc

    def _run(self):
        print("app running just fine!")

    def _arun(self):
        raise NotImplementedError("this tool does not support async")