from langchain_core.prompts import ChatPromptTemplate


chat_tempalte =ChatPromptTemplate[(
    ('system','You are a healful  {domain} expart'),
    ('human','Explain in simple terms, what is {topic}')
    

)]

prompt =chat_tempalte.invoke({'domain': 'cricket', 'topic': 'Dusra'})
print(prompt)