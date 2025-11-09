import streamlit as st
import json
import os
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage

# Load HF token
load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Load JSON prompt template
with open("prompt_template.json", "r", encoding="utf-8") as f:
    template_data = json.load(f)

prompt_template = template_data["prompt_template"]

# Initialize HuggingFace model through LangChain
hf_llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=token,
    task="chat-completion"
)

llm = ChatHuggingFace(llm=hf_llm)

# Streamlit UI
st.header("Research Paper Explainer")

paper = st.selectbox("Select Paper", [
    "Select...",
    "Attention Is All You Need (Transformers)",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models Are Few-shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis",
    "Word2Vec: Efficient Estimation of Word Representations"
])

style = st.selectbox("Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])
length = st.selectbox("Length", ["Short", "Medium", "Long"])
extra = st.text_area("Extra instructions (optional):")

if st.button("Generate") and paper != "Select...":

    # Fill JSON template
    final_prompt = prompt_template.format(
        paper_name=paper,
        style=style,
        length=length,
        user_input=extra
    )

    with st.spinner("Generating response..."):
        res = llm.invoke([HumanMessage(content=final_prompt)])

    st.subheader("✅ Output:")
    st.write(res.content)

