from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel, EmailStr,Field

load_dotenv()
model =ChatOpenAI()

# Schema 
json_schema={
  "title": "Student",
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "type": "string",
      "default": "Shahin"
    },
    "age": {
      "title": "Age",
      "type": "integer",
      "minimum": 0,
      
    },
    "email": {
      "title": "Email",
      "type": "string",
      "format": "email",
      
    },
    "cgpa": {
      "title": "Cgpa",
      "type": "number",
      "minimum": 0.0,
      "maximum": 4.0,
      "default": 3.5
    }
  },
  "required": [],

}



structured_model=model.with_structured_output(json_schema)

result=structured_model.invoke(""" The overall experience with this platform has been impressive. The interface is clean and easy to navigate, and the performance is fast even during heavy tasks. However, customer support responses were slightly delayed, which affected the overall experience. Still, the value and features provided make it a strong choice for beginners and professionals alike.
                               - reviewer: Shahin Alam.""")

print(result.name)

print(result['summary'])
print(result['sentiment'])