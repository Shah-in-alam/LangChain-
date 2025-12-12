## =============== 
#  Paraller Chain Example 
###==============
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal



from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI()
parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description="Give the sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template=' Classify the sentiment of the following feedback text into positive or negative \n{feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)


classifier_chain=prompt1 | model | parser2
result=classifier_chain.invoke({'feedback':'This is the terrible smartphone.'}).sentiment
print(result)

# print(classifier_chain.invoke({'feedback':'This is the terrible smartphone.'}))
# print(classifier_chain.invoke({'feedback':'I love the new design of your website!'}))