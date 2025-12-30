from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI()


loader=DirectoryLoader(
    path='Books',
    glob='*.pdf',
    loader_cls=PyPDFLoader,
)

docs = loader.lazy_load() # Use lazy_load for memory efficiency
# print(len(docs))
# print(docs[0].page_content)
# print(docs[325].metadata)

for  documnets in docs:
    print(documnets.metadata)