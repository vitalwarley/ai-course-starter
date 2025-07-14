"""
Stub signature required by the hidden tests:
    def refactor_code(code: str) -> dict
Returns:
    {
        "refactored": "<clean-up code>",
        "explanation": "<bullet-point rationale>"
    }
Environment:
    • Set OPENAI_API_KEY
    • pip install -r requirements.txt
"""
import os
import re
import openai

# 1️⃣ Client
openai.api_key = os.environ["OPENAI_API_KEY"]
client = openai.OpenAI()

# 2️⃣ Prompt template
SYSTEM_MSG = (
    "<PERSONA>You are a senior Python engineer.</PERSONA>"
    "<TASK>Refactoring code. </TASK>"
    "<GUIDELINES>Minimise cyclomatic complexity, duplication and nesting. If needed, add type hints to the code. </GUIDELINES>"
    "<OUTCOME>After the refactor, explain WHY your changes improve readability, testability or speed.</OUTCOME>"
)

def _ask_llm(code: str) -> str:
    "LLM call → raw markdown reply"
    resp = client.chat.completions.create(
        model="gpt-4o-mini",  # cheap + fast
        temperature=0.0,
        messages=[
            {"role": "system", "content": SYSTEM_MSG},
            {
                "role": "user",
                "content": (
                    "Here is the code:\n\n```python\n"
                    f"{code.strip()}\n```"
                    "\n\nReturn *first* the refactored code inside ```python fences, "
                    "then a plain-text explanation."
                ),
            },
        ],
    )
    return resp.choices[0].message.content

def _split_reply(text: str) -> tuple[str, str]:
    "Extract code block & explanation"
    m = re.search(r"```python(.*?)```", text, re.S)
    refactored = m.group(1).strip() if m else ""
    explanation = re.sub(r"```.*?```", "", text, flags=re.S).strip()
    return refactored, explanation

# 3️⃣ Public entrypoint
def refactor_code(code: str) -> dict:
    """Refactor <code> and explain the improvements."""
    markdown = _ask_llm(code)
    refactored, explanation = _split_reply(markdown)
    return {"refactored": refactored, "explanation": explanation}
