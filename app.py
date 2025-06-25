import os
from openai import OpenAI

client = OpenAI(
    api_key = os.getenv('CHATGPT_API_KEY')
)

completion = client.chat.completions.create(
    model = os.getenv('MODEL'),
    messages = [
        {
            "role": "system",
            "content": os.getenv('SYSTEM_PROMPT')
        },
        {
            "role": "user",
            "content": os.getenv('USER_PROMPT')
        }
    ]
)

with open(os.getenv('OUTPUT_FILE'), 'w', encoding='utf-8') as f:
    f.write(completion.choices[0].message.content)
