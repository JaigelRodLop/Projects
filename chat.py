import os
import openai

client = openai.OpenAI(
    # This is the default and can be omitted
    api_key = os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)