from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from  langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema import RunnableSequence, RunnablePassthrough,RunnableParallel

load_dotenv()

prompt1 =PromptTemplate(
    template ='Generate a tweet about {topic}.',
    input_variables = ['topic'],
  )

prompt2=PromptTemplate(
    template ='Generate a LinkedIn post about {topic}.',
    input_variables = ['topic'],
  )

# STEP 2: Define the LLM
model = ChatOpenAI()
parser = StrOutputParser()

# STEP 3: Create the runnablepass chain
joke_gen_chain.RunnableSequence(prompt1 , model, parser)

parallel_chain = RunnableParallel(
  {'joke': RunnablePassthrough(),
  'explanation':joke_gen_chain(prompt2 , model, parser  )}
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
# STEP 4: Invoke the chain

result=final_chain.invoke({'topic': 'AI advancements'})

# STEP 5: Print the result
print(result['joke'])
print(result['explanation'])