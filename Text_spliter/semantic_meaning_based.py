# splitting based on semantic meaning using langchain_experimental

from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(),breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1,
)

text="""
Artificial intelligence enables machines to perform tasks that normally require human intelligence, such as reasoning, pattern recognition, and language understanding. Machine learning, a subset of AI, allows systems to learn from data and improve over time, while deep learning uses multi-layer neural networks to handle complex, unstructured data like text, images, and audio. Data science combines programming, statistics, and domain knowledge to extract insights from data and support decision-making. Together, these fields drive modern applications such as recommendation systems, speech recognition, predictive analytics, and autonomous technologies.

Cybersecurity focuses on protecting digital systems, networks, and data from threats such as malware, phishing, and unauthorized access. Risk assessment helps organizations identify vulnerabilities, estimate impact, and prioritize security actions. Cloud computing supports scalable and secure infrastructure, while ethical AI emphasizes fairness, privacy, and transparency in model development. In the future, artificial intelligence and cybersecurity will increasingly work together, using AI to detect threats faster while applying security principles to ensure trustworthy and responsible technology deployment.
"""
# perform the splitting
result=text_splitter.split_text(text)
print(len(result))
print(result)