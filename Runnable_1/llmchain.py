from lagchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

#load the llm (GPT3.5())
llm = OpenAI(model="gpt-3.5-turbo",temperature=0.7)

# Create a Prompt Template

prompt=PromptTemplate(
    input_variables=["topic"],
    template=(
      "Suggest a catcy blog title about{topic}."
    )
)

#create an LLMChain
chain=LLMChain(llm=llm,prompt=prompt)

#Run the chain with a specific topic

topic =input('Enter a topic')
output=chain.run(topic)

print("Generated Blog Title:",output)
