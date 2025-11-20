from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-4b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()

template1 = PromptTemplate(
    template='Give me the name, age, and city of a fictional character \n {format_instructions}',
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# prompt = template1.format()
# result = model.invoke(prompt)
# parsed_output = parser.parse(result.content)  
chain = template1 | model | parser
output = chain.invoke({'topic': 'black hole'})
# print(output['name'])
# print(output['age'])
# print(output['city'])
# print(type(output))
print(output)



