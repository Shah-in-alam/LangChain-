from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path='Harry Potter 1.csv',
    encoding='utf-8',
    csv_args={'delimiter': ';'}

)
data= loader.load()
print(len(list(data)))
print(data[1].page_content)
