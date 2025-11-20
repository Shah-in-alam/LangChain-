from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-4b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)
schema=[
    ResponseSchema(name="fact_1", description="Fact 1 about the given topic}"),
    ResponseSchema(name="fact_2", description="Fact 2 about the given topic}"),
    ResponseSchema(name="fact_3", description="Fact 3 about the given topic}"),
]
parser = StructuredOutputParser.from_response_schemas(schema)   
template = PromptTemplate(
    template ='give me 3 facets about {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)
chain = template | model | parser
result=chain.invoke({'topic': 'black hole'})
# normal way#### 
# prompt = template.invoke({'topic': 'black hole'})
# result=model.invoke(prompt)
# parsed_output=parser.parse(result.content)
# print(parsed_output)

print(result)