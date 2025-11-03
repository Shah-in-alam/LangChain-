from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    model_kwargs={
        "temperature": 0.7,
        "max_new_tokens": 128
    },
    tokenizer_kwargs={"use_fast": False}  # 👈 Disable fast tokenizer
)

print(llm.invoke("What is the capital of Bangladesh?"))
