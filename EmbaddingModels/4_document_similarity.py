from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

# Correct model name
embadding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

# Use triple quotes for long text
documents = ["""
"Artificial Intelligence is not just a tool; it’s a partner that helps us reimagine what’s possible." — Sundar Pichai

Artificial Intelligence (AI) is transforming every major industry — from healthcare to education, from finance to creative arts. The core idea behind AI is simple yet powerful: machines can learn from data, identify patterns, and make decisions with minimal human intervention.

"Data is the new oil." — Clive Humby  
Just like oil fueled the industrial revolution, data fuels today’s digital revolution. The more high-quality data an AI system receives, the better it becomes at understanding context and making accurate predictions.

Machine learning is a key component of AI. It allows algorithms to improve automatically through experience. Deep learning, a specialized form of machine learning, uses neural networks that mimic the structure of the human brain. These networks can recognize speech, classify images, and even generate realistic text.

"Cybersecurity is not a product, but a process." — Bruce Schneier  
In cybersecurity, AI is used to detect anomalies, monitor threats, and prevent intrusions before they happen. By analyzing millions of network events per second, AI-driven systems can identify unusual behavior patterns that may indicate potential attacks.

Natural Language Processing (NLP) is another critical area of AI. It enables machines to understand and generate human language. For example, NLP powers virtual assistants, chatbots, and translation tools that we use every day. Embedding models, such as sentence transformers, represent text as numerical vectors — capturing meaning beyond individual words.

"The greatest danger in times of turbulence is not the turbulence; it is to act with yesterday’s logic." — Peter Drucker  
AI forces us to rethink how we work, learn, and communicate. The challenge ahead is not only to build intelligent machines but also to ensure they are used responsibly, ethically, and transparently.

"In the future, AI will continue to augment human intelligence, not replace it. It will help us solve problems that were once thought impossible — from climate change modeling to personalized education. The fusion of human creativity and artificial intelligence marks the dawn of a new era of discovery."
"""]



# User query
query = "How does artificial intelligence help in cybersecurity?"

# Create embeddings
doc_embeddings = embadding.embed_documents(documents)
query_embedding = embadding.embed_query(query)

# Compute cosine similarity
similarity = cosine_similarity([query_embedding], doc_embeddings)[0]

index,score=sorted(list(enumerate(similarity)),key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print(f"Similarity Score: {score}")