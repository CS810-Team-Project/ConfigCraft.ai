from openai import OpenAI
from dotenv import load_dotenv
import os
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam
from llama_index.agent.openai import OpenAIAssistantAgent

# Load environment variables from .env file
load_dotenv()

llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
query_rewrite_agent = OpenAIAssistantAgent.from_existing(assistant_id="asst_4ul13DeDrQBJWcQgdQ8a2nKI")
iptables_agent = OpenAIAssistantAgent.from_existing(assistant_id="asst_kVaZJPV3A6upADY42q3VqOkV")
soot_agent = OpenAIAssistantAgent.from_existing(assistant_id="asst_OQRNaqCvlFJkX4RzFIC3XUGX")
general_agent = OpenAIAssistantAgent.from_existing(assistant_id="asst_4mPnzZY1HIzX7n05JvvjpKt7")

def system_prompt(prompt):
    return ChatCompletionSystemMessageParam(role="system", content = prompt)

def user_prompt(prompt):
    return ChatCompletionUserMessageParam(role="user", content = prompt)