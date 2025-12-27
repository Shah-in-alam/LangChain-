# runnable_branch 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough,RunnableParallel,RunnableLambda,RunnableBranch


load_dotenv()

prompt2=PromptTemplate(
    template ='Write a details report on the topic: {topic}.',
    input_variables = ['topic'],
)

prompt2=PromptTemplate(
    template='Summarize the following text \n {text}.',
    input_variables=['text'],
)

model = ChatOpenAI()
parser = StrOutputParser()

report_gen_Chain=RunnableSequence(prompt2 , model, parser)
branch_Chain=RunnableBranch(
    ('lambda x: len(x.split())> 500', RunnableSequence(prompt2 , model, parser)),# if true the summarize chain will be executed
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_Chain, branch_Chain)
result = final_chain.invoke({'topic': 'Climate Change'})
print(result)