from langchain_huggingface import HuggingFaceEmbeddings

embadding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# text ="Dhaka is the capital of Bangladesh.  "

# vector = embadding.embed_query(text)
documents=[
    "Dhaka is the capital of Bangladesh.",
    "The capital of France is Paris.",
    "Berlin is the capital of Germany."
    ]
vector = embadding.embed_documents(documents)
print(str(vector))
