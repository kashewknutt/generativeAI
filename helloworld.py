import os
from openai import OpenAI

client = OpenAI(
    api_key="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"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role":"user",
            "content":"Hello World!!"
        }
    ],
    model="gpt-4",
)

print(chat_completion.choices[0].message)