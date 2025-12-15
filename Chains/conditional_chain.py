## =============== 
#  Paraller Chain Example 
###==============
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
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

prompt2=PromptTemplate(
    template="Write an appropriate response to this positive \n {feedback}",
    input_variables=['feedback']
)
prompt3=PromptTemplate(
    template="Write an appropriate response to this negative \n {feedback}",
    input_variables=['feedback']
)
# kind of like a switch statement

brach_chain=RunnableBranch(
    (lambda x:x.sentiment =='positive',prompt2 | model | parser),
    (lambda x:x.sentiment =='negative',prompt3 | model | parser),
    #lambda x: "No valid sentiment found."
    RunnableLambda(lambda x: "No valid sentiment found.")
)

conditional_chain=classifier_chain | brach_chain
result=conditional_chain.invoke({'feedback':'I love the new design of your website!'})
print(result)  # Expected output: An appropriate response to the positive feedback.
chain.get_graph().print_ascii()
