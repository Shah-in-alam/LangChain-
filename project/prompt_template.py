# prompt_template.py

template_prompt = """
You are an AI research assistant.

📄 Research Paper: {paper_name}
🎯 Explanation Style: {style}
✏️ Explanation Length: {length}

User additional input:
{user_input}

----------------------------
TASK:
Explain the research paper following the selected style and length.

Guidelines:
- Beginner-Friendly → remove jargon, explain in easy terms
- Technical → explain architectures, formulas, theory
- Code-Oriented → include pseudo-code or examples
- Mathematical → focus on equations and algorithm logic

Start your explanation below:
"""


