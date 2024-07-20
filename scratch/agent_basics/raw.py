import os
from openai import OpenAI

def main():
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=os.environ.get("OPENAI_API_URL"),
    )

    question = "Who would win a fight between Goku and One Punch Man? Keep it short"

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="Llama-3-8B-Instruct",
    )

    print(chat_completion.choices[0].message.content)