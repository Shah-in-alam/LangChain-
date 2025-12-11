### =============
### Sequential Chain Example ============= ###
###==============
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI()
prompt1=PromptTemplate(
    template='Generate a details report on  {topic}.',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}.',
    input_variables=['text']
)
parser=StrOutputParser()

chain= prompt1 | model | prompt2 | model | parser
result=chain.invoke({'topic':'Cricket'})
print(result)
# to see the chain structure
print(chain)