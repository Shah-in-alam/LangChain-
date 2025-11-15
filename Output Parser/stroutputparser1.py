from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# ---- SAFE & WORKING ----
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    provider="hf-inference",   # <<< FIX
)

template1 = PromptTemplate(
    template="Write a detailed report on the following topic: {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 5 line summary of the following text:\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

# Build a simple chain piece by piece (safe)
first = template1 | llm | parser
second = template2 | llm | parser

# run chain manually
report = first.invoke({"topic": "Artificial Intelligence"})
summary = second.invoke({"text": report})

print(summary)

