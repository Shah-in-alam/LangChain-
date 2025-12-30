from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader,WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text: \n {text}',
    input_variables=['question', 'text'],
)

loader = WebBaseLoader(
    web_paths=["https://en.wikipedia.org/wiki/Artificial_intelligence"]
)

docs = loader.load()

# print("Number of documents:", len(docs))
# print("\n--- Preview ---\n")
# print(docs[0].page_content)

chain = prompt | model | parser

result = chain.invoke({
    'question': 'What is Artificial Intelligence?',
    'text': docs[0].page_content
})
print(result)