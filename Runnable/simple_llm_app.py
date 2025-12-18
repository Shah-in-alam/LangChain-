from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm=OpenAI(model_name="gpt-3.5-turbo",  temperature=0.7)

#create a prompt template
prompt=PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}."
)

# define the input
topic =input("Enter a topic for the blog title: ")

#format the prompt with the input
formatted_prompt=prompt.format(topic=topic)

#call the llm with the formatted prompt
blog_title=llm.predict(formatted_prompt)

print("Generated Blog Title: ", blog_title)