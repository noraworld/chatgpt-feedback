import os
import subprocess
import sys
from openai import OpenAI

client = OpenAI(
    api_key = os.getenv('CHATGPT_API_KEY')
)

completion = client.chat.completions.create(
    model = "gpt-4o",
    messages = [
        {
            "role": "system",
            "content": os.getenv('PROMPT')
        },
        {
            "role": "user",
            "content": os.getenv('COMMENT')
        }
    ]
)

comment_with_feedback = f"""\
{os.getenv('COMMENT')}

{os.getenv('TEXT_BEFORE_RESULT')}
{completion.choices[0].message.content}"""

if os.getenv('DRY_RUN') != 'true':
    command = [
        "gh",
        "issue",
        "comment",
        os.getenv('ISSUE_NUMBER'),
        "--edit-last",
        "--body",
        comment_with_feedback,
        "--repo",
        os.getenv('REPOSITORY')
    ]

    result = subprocess.run(command, text = True)
    if result.returncode != 0:
        sys.exit(f"exit status is {result.returncode}")
else:
    print(comment_with_feedback)
