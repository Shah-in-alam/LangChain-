# for checking the length of text and splitting based on a specified length
#https://chunkviz.up.railway.app/ for visualization of text splitting ,overlap, etc.
# vector visulaization:https://www.vectorvisualizer.com/visualizer
#llm visualization:https://bbycroft.net/llm

from langchain.text_splitter import TextSplitter, CharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')
docs = loader.load()

spliter = CharacterTextSplitter(
    chunk_size=200, 
    chunk_overlap=0,
    separator=''
    )

result=spliter.split_documents(docs) # for text spliter_text, for pdf use split_documents, for other use split_text

print(result[1].page_content)
