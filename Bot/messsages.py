from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model =ChatOpenAI()
messages=[
    SystemMessage(conetent='You are a helpful assistance'),
    HumanMessage(content='Tell me about langchain')
]
result=model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)