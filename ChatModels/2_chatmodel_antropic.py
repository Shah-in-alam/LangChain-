from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()
modeL=ChatAnthropic(model="claude-2",temperature=0,max_tokens_to_sample=10 )
result=modeL.invoke("What is the capital of France?")
print(result.content)  # Expected output: "The capital of France is Paris."