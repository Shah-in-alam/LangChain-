from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# -------------------------
# 1. Load documents
# -------------------------
loader = TextLoader("sample.txt", encoding="utf-8")
documents = loader.load()

# -------------------------
# 2. Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)
# -------------------------

# 3. Create vector store
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(chunks, embeddings)

# 4. Create RetrievalQA chain
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever()
)
# -------------------------
# 5. Query
query = input("Enter your question: ")
answer = qa_chain.run(query)
print("Answer:", answer)
