from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
result = model.invoke("How is the current PM of Bangladesh?")
print("Response:", result.content)

