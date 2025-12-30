from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Summarize the following text \n {text}.',
    input_variables=['text'],
)

parser = StrOutputParser()

loader = TextLoader(
    "LAGraph_Detailed_Understanding.txt",
    encoding="utf-8",
)

docs = loader.load()

print(docs[0].page_content[:1000])
print(docs[0].metadata)   # should be of type Document

chain =prompt | model | parser
result= chain.invoke({'text': docs[0].page_content})
print(result)

chain = prompt | model | parser

result=chain.invoke({'text': docs[0].page_content})
print(result)