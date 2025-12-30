from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
    web_paths=[
        "https://github.com/Shah-in-alam/LangChain-/blob/main/readme.md"
    ]
)

docs = loader.load()
print(len(docs))
print(docs[0].page_content)
