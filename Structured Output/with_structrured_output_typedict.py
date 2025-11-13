from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()
model =ChatOpenAI()

# Schema 
class Review(TypedDict):
    key_themes: Annotated[str,"Write down all the key themes discussed in the review"] 
    summary: Annotated[str,"A brief summary of the review"]
    sentiment: Annotated[str,"Return sentiment of the review either negative, positive or netural"]
    pros: Annotated[Optional[list[str]],"Write down the pros mentioned in the review"]
    cons: Annotated[Optional[list[str]],"Write down the cons mentioned in the review"]


structured_model=model.with_structured_output(Review)

result=structured_model.invoke(""" The overall experience with this platform has been impressive. The interface is clean and easy to navigate, and the performance is fast even during heavy tasks. However, customer support responses were slightly delayed, which affected the overall experience. Still, the value and features provided make it a strong choice for beginners and professionals alike.""")

print(result)
print(result['summary'])
print(result['sentiment'])