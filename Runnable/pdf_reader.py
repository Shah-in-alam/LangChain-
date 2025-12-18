import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document

# -------------------------
# 1. Load document safely
# -------------------------
loader = TextLoader("sample.txt", encoding="utf-8")
documents = loader.load()

# Optional: basic document validation
if not documents:
    raise ValueError("No documents loaded")

# -------------------------
# 2. Split documents
# -------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)

# -------------------------
# 3. Create vector store
# -------------------------
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# -------------------------
# 4. Secure prompt template
# -------------------------
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a security-aware assistant. "
        "Answer ONLY using the provided context. "
        "If the answer is not present, say: 'I don't know.'"
    ),
    (
        "human",
        "Question: {question}\n\nContext:\n{context}"
    )
])

# -------------------------
# 5. Query
# -------------------------
query = "What is the main topic of the document?"
docs = retriever.invoke(query)

# Limit exposure (defense-in-depth)
context = "\n\n".join(
    doc.page_content[:1000] for doc in docs
)

# -------------------------
# 6. Secure LLM
# -------------------------
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
)

chain = prompt | llm

response = chain.invoke({
    "question": query,
    "context": context
})

print(response.content)
# Note: Ensure environment variables for API keys are set securely.