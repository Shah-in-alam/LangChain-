from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",  # 
    task="text-generation",
    temperature=0.7,
    max_new_tokens=128,
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of Bangladesh?")
print("Response:", result.content)



