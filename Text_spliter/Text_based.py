

from langchain.text_splitter import TextSplitter, CharacterTextSplitter,RecursiveCharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader

text="""
Debt vs Equity: Debt is borrowed money with fixed interest and maturity. Equity represents
ownership with no fixed payments. Debt is less risky than equity.
Money market vs Capital market: Money market provides short-term funds. Capital market provides
long-term financing.
Income statement: Shows revenues, expenses, and profit over a period. Measures company
performance.
Balance sheet: Shows assets, liabilities, and equity at one point in time. Represents financial
position.
Statement of cash flows: Shows cash inflows and outflows. Helps assess liquidity and cash
management.
Current ratio: Measures ability to meet short-term obligations. Higher value means better liquidity.
Quick ratio: Measures liquidity without inventory. More conservative than current ratio.
Debt ratio: Shows how much of assets are financed by debt. Higher ratio means higher risk.
Times interest earned: Shows ability to pay interest expenses. Higher value means lower defaul
"""
# Initialize the loader and load the document
spliter =RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0,
    separators=["\n\n", "\n", " ", ""]

)

# perform the splitting
result=spliter.split_text(text)
print(len(result))
print(result)