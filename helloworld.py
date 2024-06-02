import os
from openai import OpenAI

client = OpenAI(
    api_key="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"
)
message = ""
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role":"user",
            "content":message
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message)