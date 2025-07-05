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

dirpath = os.path.dirname(os.getenv('OUTPUT_FILE'))
if dirpath:
    os.makedirs(dirpath, exist_ok=True)

with open(os.getenv('OUTPUT_FILE'), 'w', encoding='utf-8') as f:
    content = ''

    if os.getenv('TEXT_BEFORE_RESULT') != '' and os.getenv('TEXT_BEFORE_RESULT') is not None:
        content += os.getenv('TEXT_BEFORE_RESULT') + os.linesep

    content += completion.choices[0].message.content

    if os.getenv('TEXT_AFTER_RESULT') != '' and os.getenv('TEXT_AFTER_RESULT') is not None:
        content = content.rstrip(os.linesep) + os.linesep + os.linesep + os.getenv('TEXT_AFTER_RESULT')

    if os.getenv('TRAILING_NEWLINE') == 'true':
        content = content.rstrip(os.linesep) + os.linesep

    f.write(content)
