from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from  langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema import RunnableSequence, RunnableParallel

load_dotenv()

#step 1: Define the prompt template
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

# STEP 3: Create the RunnableParallel chain
parallel_chain = RunnableParallel(
    {
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
    }
)

# STEP 4: Invoke the chain
result = parallel_chain.invoke({'topic': 'AI advancements'})


# STEP 5: Print the result
print(result)