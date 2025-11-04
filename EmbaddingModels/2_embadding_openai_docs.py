from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embadding =OpenAIEmbeddings(model='text-embedding-3-largest', dimensions=32)
documents=[
    "Dhaka is the capital of Bangladesh.",
    "The capital of France is Paris.",
    "Berlin is the capital of Germany."
    ]

result = embadding.embed_documents(documents)   

print(result)