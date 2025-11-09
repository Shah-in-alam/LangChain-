# prompt_generator.py

import json
from prompt_template import template_prompt

data = {
    "template_name": "research_paper_explainer_v1",
    "description": "Reusable prompt template for explaining research papers",
    "variables": ["paper_name", "style", "length", "user_input"],
    "prompt_template": template_prompt
}

with open("prompt_template.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("✅ Template saved as prompt_template.json")

