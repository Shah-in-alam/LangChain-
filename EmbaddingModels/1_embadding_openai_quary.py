from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embadding =OpenAIEmbeddings(model='text-embedding-3-largest', dimensions=32)
vector = embadding.embed_query("Dhaka is the capital of Bangladesh?")

print(vector)
