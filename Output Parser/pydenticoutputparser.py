from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-4b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name :str =Field(description='Name of the person')
    age: int =Field(description='Age of the person')
    city: str =Field(description='City of the person')  

parser = PydanticOutputParser(pydantic_object=Person)
template = PromptTemplate(
    template="""Generate the name, age and city of a fictional {place} person
     {format_instructions}""",
    input_variables=['place'],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
# prompt = template.iunvoke({'place': 'Italian'})
# response = model.predict(prompt)
# person = parser.parse(response)
# print(person)
chain = template | model | parser
person = chain.invoke({'place': 'Italian'})
print(person)
    


    
  