from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough,RunnableParallel,RunnableLambda

load_dotenv()

def word_count(text):
        return len(text.split())

prompt =PromptTemplate(
    template ='Generate a joke about {topic}.',
    input_variables = ['topic'],
  )

# STEP 2: Define the LLM
model = ChatOpenAI()
parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt , model, parser)

# STEP 3: Create the runnablelambda chain
parrallel_chain = RunnableParallel(
    {'joke': RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)}
    )

final_chain = RunnableSequence(joke_gen_chain, parrallel_chain)
result = final_chain.invoke({'topic': 'AI'})
final_result ="""{} \n Word Count: {}""".format(result['joke'], result['word_count'])
print(final_result)