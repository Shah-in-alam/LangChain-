from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from  langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema import RunnableSequence

load_dotenv()

#Step: Define the prompt template
prompt =PromptTemplate(
    template ='Generate a tweet about {topic}.',
    input_variables = ['topic'],
  )